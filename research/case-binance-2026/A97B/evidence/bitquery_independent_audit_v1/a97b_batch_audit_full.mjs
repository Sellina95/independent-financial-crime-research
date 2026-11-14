import fs from 'node:fs';
import crypto from 'node:crypto';
import { Client, StreamableHTTPClientTransport } from '@modelcontextprotocol/client';

const DIR = 'a97b_batch_audit_full_1015_v1';
fs.mkdirSync(DIR, {recursive:true});

const csv = fs.readFileSync('reconciliation_full_1015.csv','utf8');
const lines = csv.trim().split(/\r?\n/);
const headers = lines.shift().split(',');

function parseCSV(line) {
  return line.match(/("(?:[^"]|"")*"|[^,]*)(,|$)/g)
    ?.map(x=>x.replace(/,$/,'').replace(/^"|"$/g,'').replace(/""/g,'"')) || [];
}

const records = lines.map(line=>{
  const values=parseCSV(line);
  return Object.fromEntries(headers.map((h,i)=>[h,values[i]||'']));
});

const expected=new Map();
for(const r of records){
  const tx=r.tx_hash?.toLowerCase();
  if(!/^0x[a-f0-9]{64}$/.test(tx) || !/^\d+$/.test(r.expected_wei||'')) continue;
  if(expected.has(tx) && expected.get(tx)!==r.expected_wei)
    throw Error('CONFLICTING_EXPECTED_WEI: '+tx);
  expected.set(tx,r.expected_wei);
}

if(!expected.size) throw Error('No valid transactions in reconciliation.csv');

const token=process.env.BITQUERY_TOKEN;
if(!token) throw Error('Missing BITQUERY_TOKEN');

const client=new Client({name:'a97b-batch-audit',version:'1.0.0'});
const transport=new StreamableHTTPClientTransport(
  new URL('https://mcp.bitquery.io'),
  {requestInit:{headers:{Authorization:`Bearer ${token}`}}}
);

const weth='0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2';
const topic='0x7fcf532c15f0a6db0bd6d0e038bea71d30d808c7d98cb3bf7268a95bf5081b65';
const txs=[...expected.keys()];
const batches=[];
for(let i=0;i<txs.length;i+=50) batches.push(txs.slice(i,i+50));

function sha(data){return crypto.createHash('sha256').update(data).digest('hex');}

try{
  await client.connect(transport);
  console.log('TOTAL_ELIGIBLE_TX:',txs.length);
  console.log('BATCHES:',batches.length);

  for(let i=0;i<batches.length;i++){
    const file=`${DIR}/batch_${String(i+1).padStart(3,'0')}.json`;
    if(fs.existsSync(file)){
      console.log('EXISTING_BATCH:',i+1);
      continue;
    }

    const result=await client.callTool({
      name:'eth_tx_events',
      arguments:{
        tx_hash:batches[i].join('|'),
        event:'Withdrawal',
        only_successful:1,
        limit:1000
      }
    });

    if(result.isError) throw Error('TOOL_ERROR_BATCH_'+(i+1));

    const raw=JSON.stringify({
      requested_txs:batches[i],
      response:result
    },null,2);

    fs.writeFileSync(file,raw,{flag:'wx'});
    console.log('SAVED_BATCH:',i+1,'/',batches.length);

    if(i<batches.length-1)
      await new Promise(resolve=>setTimeout(resolve,6500));
  }

  const events=[];
  const manifest=[];

  for(let i=0;i<batches.length;i++){
    const file=`${DIR}/batch_${String(i+1).padStart(3,'0')}.json`;
    const raw=fs.readFileSync(file,'utf8');
    const saved=JSON.parse(raw);
    if(saved.requested_txs.join('|')!==batches[i].join('|'))
      throw Error('BATCH_INPUT_MISMATCH_'+(i+1));

    manifest.push({file,sha256:sha(raw)});

    for(const item of saved.response.content||[]){
      if(item.type!=='text')continue;
      const parsed=JSON.parse(item.text);
      if(Array.isArray(parsed))events.push(...parsed);
      else if(Array.isArray(parsed.rows) && Array.isArray(parsed.columns)){
        for(const row of parsed.rows)
          events.push(Object.fromEntries(parsed.columns.map((c,j)=>[c,row[j]])));
      } else events.push(parsed);
    }
  }

  const report=[];
  for(const tx of txs){
    const found=events.filter(e=>
      e.Tx?.toLowerCase()===tx &&
      e.Emitter?.toLowerCase()===weth &&
      e.Topic0?.toLowerCase()===topic &&
      e.Signature==='Withdrawal(address,uint256)' &&
      e.TxSuccess===1 &&
      e.Reverted===0 &&
      e.Removed===0
    );

    const actual=found.map(e=>{
      const data=e.Data;
      if(!/^0x[0-9a-f]{64}$/i.test(data||''))return null;
      return BigInt(data).toString();
    });

    const verdict=found.length===1 && actual[0]===expected.get(tx)
      ? 'MATCH':'REVIEW_REQUIRED';

    report.push({tx,expected_wei:expected.get(tx),
      actual_wei:actual.join('|'),event_count:found.length,verdict});
  }

  const output=['tx_hash,expected_wei,actual_wei,event_count,verdict',
    ...report.map(r=>Object.values(r).join(','))].join('\n')+'\n';

  fs.writeFileSync(`${DIR}/audit_results.csv`,output);
  fs.writeFileSync(`${DIR}/manifest.json`,
    JSON.stringify({input_sha256:sha(csv),batches:manifest,
      results_sha256:sha(output)},null,2));

  console.log('MATCH:',report.filter(r=>r.verdict==='MATCH').length);
  console.log('REVIEW_REQUIRED:',report.filter(r=>r.verdict!=='MATCH').length);
  console.log('RESULT:',`${DIR}/audit_results.csv`);
  console.log('MANIFEST:',`${DIR}/manifest.json`);

} finally {
  await transport.close();
}
