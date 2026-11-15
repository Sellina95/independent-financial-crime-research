import json, re, hashlib, threading
from pathlib import Path
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlsplit, parse_qs
import importlib.util

ROOT = Path(__file__).resolve().parent
ORIGINAL_MAP = (
    ROOT.parent
    / "analysis"
    / "master_timeline_v0"
    / "BINANCE14_MASTER_FLOW_MAP_V1.html"
)

BASE = ROOT / "BASE_EVENTS_V1.json"
DRAFT = ROOT / "DRAFT_EVENTS_V1.json"
REVIEWS = ROOT / "ROUTE_REVIEW_V1.json"
LOCK = threading.Lock()
ADDRESS = re.compile(r"^0x[a-fA-F0-9]{40}$")

def key(value):
    return str(value or "").lower()

HASH = re.compile(r"^0x[a-fA-F0-9]{64}$")

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def save(path, value):
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(path)

def events():
    return load(BASE) + load(DRAFT)


def registration_status(tx, src, dst, asset, contract, amount, log_index=None):
    from decimal import Decimal, InvalidOperation

    tx = key(tx)
    src = key(src)
    dst = key(dst)
    asset = key(asset)
    contract = key(contract)

    # ERC-20 logIndex is a transaction-scoped event identifier.
    # Do not equate raw token units with human-readable amounts.
    if log_index is not None:
        expected_id = f"{tx}:log:{int(log_index)}"
        matching_ids = [
            x for x in events()
            if key(x.get("event_id")) == expected_id
        ]

        if matching_ids:
            for x in matching_ids:
                if (
                    key(x.get("tx_hash")) != tx
                    or key(x.get("from_address")) != src
                    or key(x.get("to_address")) != dst
                    or (
                        contract
                        and key(x.get("asset_contract")) != contract
                    )
                ):
                    return "REVIEW_REQUIRED"

            return "REGISTERED"

    same_pair = [
        x for x in events()
        if key(x.get("tx_hash")) == tx
        and key(x.get("from_address")) == src
        and key(x.get("to_address")) == dst
    ]

    if not same_pair:
        return "NEW"

    relevant = []
    for x in same_pair:
        existing_contract = key(x.get("asset_contract"))
        existing_asset = key(x.get("asset_as_recorded"))

        if contract and existing_contract:
            same_asset = contract == existing_contract
        else:
            same_asset = asset == existing_asset

        if same_asset:
            relevant.append(x)

    if not relevant:
        return "NEW"

    for x in relevant:
        previous = (
            x.get("amount_display_as_recorded")
            or x.get("amount_raw")
        )
        try:
            if Decimal(str(previous)) == Decimal(str(amount)):
                return "REGISTERED"
        except (InvalidOperation, TypeError, ValueError):
            pass

    # Same TX, addresses and asset, but a differing amount.
    # Without logIndex identity this cannot be safely inserted.
    return "REVIEW_REQUIRED"


def normalized(row):
    return {
        "event_id": row.get("event_id", ""),
        "tx_hash": row.get("tx_hash", ""),
        "block": row.get("block", ""),
        "utc": row.get("utc_as_recorded", ""),
        "from": row.get("from_address", ""),
        "to": row.get("to_address", ""),
        "asset": row.get("asset_as_recorded", ""),
        "contract": row.get("asset_contract", ""),
        "amount": row.get("amount_display_as_recorded", "") or row.get("amount_raw", ""),
        "status": row.get("evidence_status", ""),
        "category": row.get("category", ""),
        "log_index": row.get("log_index"),
        "evidence_origin": row.get(
            "evidence_origin", "LEGACY_REGISTER"
        )
    }

HTML = r'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Binance 14 · Research Workspace</title>
<style>
body{margin:0;background:#10151c;color:#edf2f6;font:14px/1.55 system-ui,sans-serif}
header,main{max-width:1250px;margin:auto;padding:22px}
h1{font-size:24px;margin:0}h2{font-size:17px}
small,.muted{color:#aab8c8}
nav{display:flex;gap:10px;flex-wrap:wrap;margin:20px 0}
button,input,select{background:#263443;color:#fff;border:1px solid #536273;
padding:10px;border-radius:7px;font:inherit}
button{cursor:pointer}
button:hover{border-color:#d8b27d}
input{width:100%;box-sizing:border-box}
.panel{background:#1b232e;border:1px solid #364451;border-radius:12px;padding:18px;margin:14px 0}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:15px}
.stats{display:flex;gap:12px;flex-wrap:wrap}
.stat{background:#263443;border-radius:8px;padding:12px}
.stat b{font-size:20px}
.record{border-bottom:1px solid #364451;padding:10px 0;overflow-wrap:anywhere}
.record:last-child{border:0}
a{color:#d8b27d}
.click{cursor:pointer;color:#d8b27d;overflow-wrap:anywhere}
.row{display:flex;gap:8px;flex-wrap:wrap;margin:8px 0}
.row>*{flex:1;min-width:130px}
.hidden{display:none}
label{display:block;margin:9px 0;color:#cbd5df}
.notice{padding:12px;background:#332e22;border-radius:8px;color:#ead9bd}
strong{color:#f3f7fa}
@media(max-width:800px){.grid{grid-template-columns:1fr}}
</style></head><body>
<header><small>INDEPENDENT RESEARCH · LOCAL WORKSPACE</small>
<h1>🪙 Binance 14 · Investigation Workspace</h1>
<p class="muted">조사 중인 거래와 경로를 기록하는 연구 화면. 공개 웹사이트와 연결되지 않습니다.</p>
<div class="stats" id="stats"></div>
<nav>
<button onclick="show('map')">🕸️ Flow Map</button>
<button onclick="show('timeline')">🕒 Transaction Timeline</button>
<button onclick="show('add')">＋ Add Transaction</button>
<button onclick="show('review')">✓ Route Review</button>
</nav>
<div class="notice">직접 입력한 거래는 DRAFT입니다. TX 해시 형식 검사는 블록체인 영수증 검증이 아닙니다. 완료 체크도 공개 승인이나 자금 출처 입증을 의미하지 않습니다.</div>
</header>
<main>
<section id="map" class="panel">
<h2>🕸️ Binance 14 · Master Flow Map</h2>
<p class="muted">
Original research visualization · Existing audited dataset.
New DRAFT transactions are integrated into this research graph.
</p>
<iframe
    src="/original-map"
    title="Binance 14 Master Flow Map"
    style="width:100%;height:950px;border:1px solid #364451;
           border-radius:10px;background:#10151c"
></iframe>
<div id="selectedTitle" class="hidden"></div>
<div id="mapContent" class="hidden"></div>
<input id="search" class="hidden" aria-label="Legacy search">
<div id="matches" class="hidden"></div>
</section>
<section id="timeline" class="panel hidden">
<h2>Transaction Timeline</h2>
<p class="muted">기존 거래와 신규 DRAFT를 시간순으로 표시합니다.</p>
<input id="timeSearch" placeholder="주소 / TX 해시 / 자산으로 검색" oninput="renderTimeline()">
<div id="timeContent"></div>
</section>
<section id="add" class="panel hidden">
<h2>Add Transaction</h2>
<p class="muted">새 이동 기록을 추가하면 지도와 타임라인에 함께 반영됩니다.</p>
<form id="eventForm">
<input type="hidden" name="lookup_kind" value="">
<input type="hidden" name="log_index" value="">
<label>Transaction Hash<input name="tx" required placeholder="0x + 64 hex characters"></label>
<button type="button" id="fetchTx">Fetch & Verify Transaction</button>
<div id="lookupResult" class="panel hidden"></div>
<div class="grid">
<label>From Address<input name="from" required placeholder="0x..."></label>
<label>To Address<input name="to" required placeholder="0x..."></label>
<label>Block Number<input name="block" required type="number" min="1"></label>
<label>UTC Time<input name="utc" required type="datetime-local" step="1"></label>
<label>Token Symbol<input name="asset" required placeholder="ETH / USDT / ..."></label>
<label>Amount<input name="amount" required placeholder="123.456"></label>
<label>Token Contract (optional)<input name="contract" placeholder="0x... / blank for ETH"></label>
</div>
<button type="submit">Save as DRAFT</button>
</form>
<p id="addMessage"></p>
</section>
<section id="review" class="panel hidden">
<h2>Route Review · 조사 범위 기록</h2>
<p class="muted">주소 전체가 아니라, 지정한 자산과 블록 범위를 대상으로 기록합니다.</p>
<form id="reviewForm">
<label>Wallet Address<input name="address" required placeholder="0x..."></label>
<label>Asset<input name="asset" required placeholder="ETH / USDT / ..."></label>
<div class="grid">
<label>From Block<input name="start" type="number" min="1" required></label>
<label>To Block<input name="end" type="number" min="1" required></label>
</div>
<label>Evidence / Research Notes<input name="notes" required placeholder="검증한 파일, TX, 남은 한계"></label>
<button type="submit">Mark Scope Reviewed</button>
</form>
<p id="reviewMessage"></p>
<div id="reviewContent"></div>
</section>
</main>
<script>
let E=[], R=[], selected="0x28c6c06298d514db089934071355e5743bf21d60";
const $=id=>document.getElementById(id);
const esc=s=>String(s??"").replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
const short=s=>s&&s.length>22?s.slice(0,10)+"…"+s.slice(-8):s;
const key=s=>String(s||"").toLowerCase();
function show(id){
 for(const name of ["map","timeline","add","review"])$(name).classList.toggle("hidden",name!==id);
 if(id==="timeline")renderTimeline();
}
async function refresh(){
 const response=await fetch("/api/data");
 const data=await response.json();
 E=data.events; R=data.reviews;
 const addresses=new Set(E.flatMap(e=>[key(e.from),key(e.to)]).filter(Boolean));
 const hashes=new Set(E.map(e=>key(e.tx_hash)).filter(Boolean));
 const drafts=E.filter(e=>e.status==="DRAFT").length;
 $("stats").innerHTML=[
 ["Addresses",addresses.size],["Transfer records",E.length],
 ["Transaction hashes",hashes.size],["Draft events",drafts],
 ["Reviewed scopes",R.length]
 ].map(([k,v])=>`<div class="stat"><b>${v.toLocaleString()}</b><br><small>${k}</small></div>`).join("");
 renderMap();renderTimeline();renderReviews();
}
function wallet(s){selected=key(s);show("map");renderMap();}
function renderMap(){
 const found=E.filter(e=>key(e.from)===selected||key(e.to)===selected);
 const neighbors=new Map();
 for(const e of found){
  const a=key(e.from)===selected?key(e.to):key(e.from);
  if(!neighbors.has(a))neighbors.set(a,{out:0,in:0});
  neighbors.get(a)[key(e.from)===selected?"out":"in"]++;
 }
 $("selectedTitle").textContent="Selected wallet · "+short(selected);
 $("mapContent").innerHTML=
 `<p><small>${esc(selected)}</small></p><p>Incoming: <b>${found.filter(e=>key(e.to)===selected).length}</b> · Outgoing: <b>${found.filter(e=>key(e.from)===selected).length}</b></p>`+
 `<h2>Connected wallets (${neighbors.size})</h2>`+
 [...neighbors.entries()].sort((a,b)=>(b[1].in+b[1].out)-(a[1].in+a[1].out)).map(([a,n])=>
 `<div class="record"><span class="click" data-wallet="${esc(a)}">${esc(short(a))}</span> <small>→ ${n.out} / ← ${n.in}</small></div>`).join("")+
 `<h2>Transfer records · first 30</h2>`+
 found.slice(0,30).map(record).join("");
 $("mapContent").querySelectorAll("[data-wallet]").forEach(el=>el.onclick=()=>wallet(el.dataset.wallet));
}
function record(e){
 return `<div class="record"><strong>${esc(e.asset)}</strong> · ${esc(e.amount)} <small>[${esc(e.status)}]</small><br>`+
 `<span class="click" data-wallet="${esc(e.from)}">${esc(short(e.from))}</span> → `+
 `<span class="click" data-wallet="${esc(e.to)}">${esc(short(e.to))}</span><br>`+
 `<small>${esc(e.utc)} UTC · Block ${esc(e.block)} · ${esc(e.evidence_origin||"LEGACY_REGISTER")}${e.log_index===null||e.log_index===undefined?"":" · logIndex "+esc(e.log_index)}</small> · `+
 `<a href="https://etherscan.io/tx/${encodeURIComponent(e.tx_hash)}" target="_blank" rel="noopener">Etherscan</a></div>`;
}
function renderTimeline(){
 const q=key($("timeSearch").value);
 const found=E.filter(e=>[e.tx_hash,e.from,e.to,e.asset].some(v=>key(v).includes(q)))
 .sort((a,b)=>Number(a.block)-Number(b.block)||String(a.utc).localeCompare(String(b.utc)));
 $("timeContent").innerHTML=`<p>${found.length} records · first 100 shown</p>`+found.slice(0,100).map(record).join("");
 $("timeContent").querySelectorAll("[data-wallet]").forEach(el=>el.onclick=()=>wallet(el.dataset.wallet));
}
function searchWallets(){
 const q=key($("search").value).trim();
 if(!q){$("matches").innerHTML="";return;}
 const matches=[...new Set(E.flatMap(e=>[key(e.from),key(e.to)]))]
 .filter(a=>a.includes(q)).slice(0,20);
 $("matches").innerHTML=matches.map(a=>`<div class="record click" data-wallet="${esc(a)}">${esc(a)}</div>`).join("");
 $("matches").querySelectorAll("[data-wallet]").forEach(el=>el.onclick=()=>wallet(el.dataset.wallet));
}
function renderReviews(){
 $("reviewContent").innerHTML="<h2>Reviewed scopes</h2>"+
 R.map(r=>`<div class="record"><strong>${esc(short(r.address))}</strong> · ${esc(r.asset)} · blocks ${r.start}–${r.end}<br><small>${esc(r.notes)} · REVIEWED, not published</small></div>`).join("");
}
async function submit(path,data,msg){
 const response=await fetch(path,{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(data)});
 const body=await response.json();
 $(msg).textContent=body.message||body.error||"Unknown response";
 if(response.ok){
   await refresh();
   const frame=document.querySelector('iframe[src^="/original-map"]');
   if(frame)frame.src="/original-map?revision="+Date.now();
 }
}

$("fetchTx").onclick=async ()=>{
 const form=$("eventForm");
 const hash=form.elements.namedItem("tx").value.trim();
 const box=$("lookupResult");
 box.classList.remove("hidden");
 box.replaceChildren();
 box.textContent="Checking Ethereum transaction and receipt…";

 try{
  const response=await fetch(
    "/api/lookup?tx="+encodeURIComponent(hash)
  );
  const data=await response.json();

  if(!response.ok)
   throw new Error(data.error||"Lookup failed");

  box.replaceChildren();

  const heading=document.createElement("h3");
  heading.textContent="Ethereum Mainnet · Confirmed receipt";
  box.append(heading);

  const summary=document.createElement("p");
  summary.textContent=
   "Block "+data.block+" · "+data.utc+
   " UTC · "+data.transfers.length+" transfer candidate(s)";
  box.append(summary);

  const warning=document.createElement("p");
  warning.className="notice";
  warning.textContent=
   "Receipt success does not establish Binance 14 incident attribution. "+
   "Internal ETH traces are not included. No data saved yet.";
  box.append(warning);

  const context=data.execution_context||{};
  const withdrawals=context.weth_withdrawals||[];
  const deliveries=context.reported_internal_eth||[];

  if(withdrawals.length||deliveries.length){
   const title=document.createElement("h3");
   title.textContent="WETH → ETH Execution Context";
   box.append(title);

   withdrawals.forEach(w=>{
    const div=document.createElement("div");
    div.className="record";
    div.textContent=
     "WETH Withdrawal · "+w.amount_eth+
     " ETH · logIndex "+w.log_index+
     " · Withdrawer: "+w.withdrawer+
     " · Receipt verified";
    box.append(div);
   });

   deliveries.forEach(d=>{
    const div=document.createElement("div");
    div.className="record";
    div.textContent=
     "Reported internal ETH · "+d.amount_display+
     " ETH · "+d.sender+" → "+d.receiver+
     " · "+d.precision+
     " · Exact internal trace NOT verified"+
     " · Incident attribution NOT established";
    box.append(div);
   });

   const note=document.createElement("p");
   note.className="notice";
   note.textContent=
    "Execution context only. Not an additional "+
    "verified inflow. Internal ETH is not selectable "+
    "or saved automatically.";
   box.append(note);
  }

  if(data.transfers.length===0){
   const empty=document.createElement("p");
   empty.textContent=
    "No top-level native ETH or ERC-20 Transfer logs found.";
   box.append(empty);
  }

  data.transfers.forEach((item,index)=>{
   const entry=document.createElement("div");
   entry.className="record";

   const info=document.createElement("p");
   info.textContent=
    (index+1)+". "+item.kind+
    " · "+(item.amount??("RAW "+item.raw_amount))+
    " "+item.asset+
    " · "+item.from+" → "+item.to+
    (item.log_index===null?"":" · logIndex "+item.log_index);
   entry.append(info);

   const select=document.createElement("button");
   select.type="button";
   const registration=item.registration_status||"NEW";
   select.textContent=
    registration==="REGISTERED"
     ?"Already Registered · No Action Needed"
    :registration==="REVIEW_REQUIRED"
     ?"Manual Audit Required · Possible Existing Route"
    :item.selectable
     ?"Use this transfer"
     :"Manual audit required";
   select.disabled=!item.selectable;

   select.onclick=()=>{
    const fields={
     tx:data.tx_hash,
     from:item.from,
     to:item.to,
     block:String(data.block),
     utc:data.utc,
     asset:item.asset,
     amount:item.amount,
     contract:item.contract,
     lookup_kind:item.kind,
     log_index:item.log_index===null?"":String(item.log_index)
    };
    for(const [name,value] of Object.entries(fields)){
     form.elements.namedItem(name).value=value;
    }
    $("addMessage").textContent=
     "Fields populated from receipt. NOT SAVED. "+
     "Review evidence before Save as DRAFT.";
   };

   entry.append(select);
   box.append(entry);
  });

 }catch(error){
  box.textContent="Lookup failed: "+error.message;
 }
};

$("eventForm").addEventListener("input",ev=>{
 if(ev.target.name==="lookup_kind"||ev.target.name==="log_index")
  return;
 $("eventForm").elements.namedItem("lookup_kind").value="";
 $("eventForm").elements.namedItem("log_index").value="";
});

$("eventForm").onsubmit=async ev=>{
 ev.preventDefault();
 const f=Object.fromEntries(new FormData(ev.target).entries());
 await submit("/api/event",f,"addMessage");
};
$("reviewForm").onsubmit=async ev=>{
 ev.preventDefault();
 const f=Object.fromEntries(new FormData(ev.target).entries());
 await submit("/api/review",f,"reviewMessage");
};
refresh().catch(e=>alert("Cannot load research data: "+e));
</script></body></html>'''


def render_original_map():
    import copy

    html = ORIGINAL_MAP.read_text(encoding="utf-8")
    pattern = (
        r'(<script type="application/json" id="dataset">)'
        r'(.*?)'
        r'(</script>)'
    )
    match = re.search(pattern, html, re.DOTALL)
    if not match:
        raise RuntimeError("Original map dataset missing")

    dataset = json.loads(match.group(2))
    original_edges = dataset["edges"]
    base_rows = load(BASE)

    # Prevent silent divergence between the two originals.
    original_ids = [e["event_id"] for e in original_edges]
    base_ids = [e["event_id"] for e in base_rows]

    if (
        len(original_ids) != len(base_ids)
        or len(set(original_ids)) != len(original_ids)
        or set(original_ids) != set(base_ids)
    ):
        raise RuntimeError("Original map / base ledger mismatch")

    dataset = copy.deepcopy(dataset)
    edges = dataset["edges"]

    known_ids = {e["event_id"] for e in edges}

    for draft in load(DRAFT):
        eid = draft["event_id"]
        if eid in known_ids:
            raise RuntimeError("Duplicate event ID: " + eid)
        known_ids.add(eid)

        edges.append({
            "edge_id": "DRAFT-" + eid[-12:],
            "event_id": eid,
            "tx_hash": draft["tx_hash"],
            "block": draft["block"],
            "utc_as_recorded": draft["utc_as_recorded"],
            "from_address": draft["from_address"],
            "to_address": draft["to_address"],
            "asset_as_recorded": draft["asset_as_recorded"],
            "asset_contract": draft.get("asset_contract", ""),
            "amount_raw": draft.get("amount_raw", ""),
            "amount_display_as_recorded":
                draft.get("amount_display_as_recorded", ""),
            "category": "manual_candidate",
            "evidence_status": "DRAFT",
            "incident_attribution": "UNKNOWN",
            "evidence_id": "DRAFT_NOT_VERIFIED"
        })

    # Reconstruct node summaries from event rows.
    nodes = {
        n["address"].lower(): n
        for n in dataset["nodes"]
    }

    for e in edges:
        for field in ("from_address", "to_address"):
            address = e[field].lower()
            if address not in nodes:
                nodes[address] = {
                    "address": address,
                    "research_label": "",
                    "wallet_identity": "NOT_ATTRIBUTED",
                    "incident_attribution": "UNKNOWN",
                    "research_coverage": "NOT_ASSESSED"
                }

    incoming = {}
    outgoing = {}

    for address in nodes:
        incoming[address] = []
        outgoing[address] = []

    for e in edges:
        outgoing[e["from_address"].lower()].append(e)
        incoming[e["to_address"].lower()].append(e)

    for address, n in nodes.items():
        ins = incoming[address]
        outs = outgoing[address]
        relevant = ins + outs
        blocks = [int(e["block"]) for e in relevant]

        n["incoming_events"] = str(len(ins))
        n["outgoing_events"] = str(len(outs))
        n["incoming_unique_txs"] = str(
            len({e["tx_hash"] for e in ins})
        )
        n["outgoing_unique_txs"] = str(
            len({e["tx_hash"] for e in outs})
        )
        n["assets_observed"] = "|".join(sorted({
            e["asset_as_recorded"] for e in relevant
        }))
        n["event_evidence_statuses"] = "|".join(sorted({
            e["evidence_status"] for e in relevant
        }))
        n["first_block_in_dataset"] = str(min(blocks)) if blocks else ""
        n["last_block_in_dataset"] = str(max(blocks)) if blocks else ""

    dataset["nodes"] = list(nodes.values())

    safe_json = json.dumps(
        dataset, separators=(",", ":"), ensure_ascii=False
    ).replace("<", "\\u003c")

    html = (
        html[:match.start(2)]
        + safe_json
        + html[match.end(2):]
    )

    stats = {
        "nn": len(nodes),
        "ne": len(edges),
        "nt": len({e["tx_hash"] for e in edges})
    }

    for element_id, count in stats.items():
        pattern_stat = (
            r'(<strong id="' + element_id +
            r'">)[0-9,]+(</strong>)'
        )
        html, replacements = re.subn(
            pattern_stat,
            lambda m, c=count: m.group(1) + f"{c:,}" + m.group(2),
            html
        )
        if replacements != 1:
            raise RuntimeError("Map statistic missing: " + element_id)

    # New DRAFT evidence filter.
    anchor = '<option value="RECEIPT_VERIFIED">Receipt verified</option>'
    if anchor not in html:
        raise RuntimeError("Status filter anchor missing")

    html = html.replace(
        anchor,
        anchor + '\n   <option value="DRAFT">Draft · unverified</option>',
        1
    )

    # Open the existing transaction form from the original map.
    home = '<button id="home">Binance 14</button>'
    if home not in html:
        raise RuntimeError("Original home button missing")

    html = html.replace(
        home,
        home + """
 <button type="button"
   onclick="parent.show('add')">
   + Add Transaction
 </button>""",
        1
    )

    # Distinguish unpublished drafts from existing evidence.
    html = html.replace(
        '<div class="notice">',
        '<div class="notice"><strong>RESEARCH WORKSPACE:</strong> '
        'DRAFT connections are unverified and are not published. '
        '</div>\n<div class="notice">',
        1
    )

    return html

class Handler(BaseHTTPRequestHandler):
    def respond(self, status, data, content_type="application/json"):
        body = data.encode() if isinstance(data, str) else json.dumps(data).encode()
        self.send_response(status)
        self.send_header("Content-Type", content_type + "; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = urlsplit(self.path).path
        if path == "/api/lookup":
            try:
                from pathlib import Path
                module_path = ROOT / "tx_lookup.py"
                spec = importlib.util.spec_from_file_location(
                    "binance_tx_lookup", module_path
                )
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                query = parse_qs(urlsplit(self.path).query)
                tx_hash = query.get("tx", [""])[0]
                result = module.lookup_transaction(tx_hash)

                context_path = ROOT / "weth_eth_context.py"
                context_spec = importlib.util.spec_from_file_location(
                    "binance_weth_context", context_path
                )
                context_module = importlib.util.module_from_spec(
                    context_spec
                )
                context_spec.loader.exec_module(context_module)

                receipt = module.rpc(
                    "eth_getTransactionReceipt", [tx_hash]
                )

                result["execution_context"] = (
                    context_module.build(receipt, tx_hash)
                )

                for item in result["transfers"]:
                    state = registration_status(
                        result["tx_hash"],
                        item["from"],
                        item["to"],
                        item["asset"],
                        item["contract"],
                        item["amount"] or "",
                        item.get("log_index")
                    )
                    item["registration_status"] = state
                    item["selectable"] = (
                        item["selectable"] and state == "NEW"
                    )

                return self.respond(200, result)
            except ValueError as exc:
                return self.respond(400, {"error": str(exc)})
        if path == "/":
            return self.respond(200, HTML, "text/html")
        if path == "/original-map":
            return self.respond(
                200,
                render_original_map(),
                "text/html"
            )
        if path == "/api/data":
            return self.respond(200, {
                "events": [normalized(x) for x in events()],
                "reviews": load(REVIEWS)
            })
        self.respond(404, {"error": "Not found"})

    def do_POST(self):
        path = urlsplit(self.path).path
        if path not in ("/api/event", "/api/review"):
            return self.respond(404, {"error": "Not found"})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length < 1 or length > 8192:
                raise ValueError("Invalid payload size")
            obj = json.loads(self.rfile.read(length))
            with LOCK:
                if path == "/api/event":
                    tx = obj["tx"].strip().lower()
                    src = obj["from"].strip().lower()
                    dst = obj["to"].strip().lower()
                    contract = obj.get("contract", "").strip().lower()
                    asset = obj["asset"].strip().upper()
                    amount = obj["amount"].strip()
                    block = int(obj["block"])
                    stamp = obj["utc"].strip()
                    lookup_kind = str(
                        obj.get("lookup_kind", "")
                    ).strip()
                    supplied_log = str(
                        obj.get("log_index", "")
                    ).strip()

                    if lookup_kind not in (
                        "", "NATIVE_ETH", "ERC20_TRANSFER"
                    ):
                        raise ValueError("Invalid lookup kind")

                    if not lookup_kind and supplied_log:
                        raise ValueError("Unverified log index")

                    if lookup_kind == "NATIVE_ETH" and supplied_log:
                        raise ValueError("Native ETH log index invalid")

                    if lookup_kind == "ERC20_TRANSFER":
                        if not supplied_log.isdecimal():
                            raise ValueError("ERC20 log index required")

                    log_index = (
                        int(supplied_log)
                        if supplied_log else None
                    )
                    verified_raw = ""
                    evidence_origin = "MANUAL_UNVERIFIED"
                    if not HASH.fullmatch(tx) or not ADDRESS.fullmatch(src) or not ADDRESS.fullmatch(dst):
                        raise ValueError("Invalid transaction hash or wallet address")
                    if contract and not ADDRESS.fullmatch(contract):
                        raise ValueError("Invalid token contract")
                    if block < 1 or not 1 <= len(asset) <= 30:
                        raise ValueError("Invalid block or asset")
                    dt = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
                    if dt.tzinfo is not None:
                        dt = dt.astimezone(timezone.utc).replace(tzinfo=None)
                    if not Decimal(amount).is_finite() or Decimal(amount) <= 0:
                        raise ValueError("Amount must be positive")
                    state = registration_status(
                        tx, src, dst, asset, contract, amount
                    )
                    if state == "REGISTERED":
                        raise ValueError(
                            "Already Registered: this transfer exists"
                        )
                    if state == "REVIEW_REQUIRED":
                        raise ValueError(
                            "Manual audit required: matching TX, "
                            "addresses and asset; logIndex unavailable"
                        )

                    if lookup_kind:
                        spec = importlib.util.spec_from_file_location(
                            "binance_save_verify",
                            ROOT / "tx_lookup.py"
                        )
                        module = importlib.util.module_from_spec(spec)
                        spec.loader.exec_module(module)

                        chain = module.lookup_transaction(tx)

                        if (
                            chain["block"] != block
                            or datetime.fromisoformat(chain["utc"]) != dt
                        ):
                            raise ValueError("RPC block/time mismatch")

                        matched = [
                            t for t in chain["transfers"]
                            if t["kind"] == lookup_kind
                            and t["log_index"] == log_index
                            and t["from"] == src
                            and t["to"] == dst
                            and t["contract"] == contract
                            and t["asset"] == asset
                            and t["amount"] is not None
                            and Decimal(t["amount"]) == Decimal(amount)
                            and t["selectable"]
                        ]

                        if len(matched) != 1:
                            raise ValueError(
                                "RPC event mismatch: save blocked"
                            )

                        verified_raw = matched[0]["raw_amount"]
                        evidence_origin = "ETHEREUM_RPC_RECEIPT"

                    identity = (tx, src, dst, contract or asset.lower(), amount)
                    for x in events():
                        xidentity = (
                            key(x["tx_hash"]), key(x["from_address"]), key(x["to_address"]),
                            key(x.get("asset_contract") or x["asset_as_recorded"]),
                            x.get("amount_display_as_recorded") or x.get("amount_raw")
                        )
                        if identity == xidentity:
                            raise ValueError("Possible duplicate event; nothing saved")
                    drafts = load(DRAFT)
                    if lookup_kind == "ERC20_TRANSFER":
                        event_id = f"{tx}:log:{log_index}"
                    elif lookup_kind == "NATIVE_ETH":
                        event_id = f"{tx}:native"
                    else:
                        event_id = (
                            tx + ":draft:" +
                            hashlib.sha256(
                                repr(identity).encode()
                            ).hexdigest()[:12]
                        )

                    if any(
                        key(e.get("event_id")) == event_id
                        for e in events()
                    ):
                        raise ValueError(
                            "Already Registered: event ID exists"
                        )
                    drafts.append({
                        "event_id": event_id,
                        "tx_hash": tx, "block": str(block),
                        "utc_as_recorded": dt.strftime("%Y-%m-%d %H:%M:%S"),
                        "from_address": src, "to_address": dst,
                        "asset_as_recorded": asset,
                        "asset_contract": contract,
                        "amount_raw": verified_raw,
                        "amount_display_as_recorded": amount,
                        "log_index": log_index,
                        "evidence_origin": evidence_origin,
                        "category": (
                            "rpc_receipt_candidate"
                            if lookup_kind else "manual_candidate"
                        ),
                        "evidence_status": "DRAFT",
                        "incident_attribution": "UNKNOWN"
                    })
                    save(DRAFT, drafts)
                    return self.respond(200, {"message": "DRAFT saved in research workspace. Not verified or published."})
                address = obj["address"].strip().lower()
                asset = obj["asset"].strip().upper()
                start, end = int(obj["start"]), int(obj["end"])
                notes = obj["notes"].strip()
                if not ADDRESS.fullmatch(address) or not 1 <= len(asset) <= 30 or not 1 <= start <= end:
                    raise ValueError("Invalid scope")
                if not 3 <= len(notes) <= 1000:
                    raise ValueError("Evidence notes required (3–1000 characters)")
                reviews = load(REVIEWS)
                if any((r["address"],r["asset"],r["start"],r["end"]) == (address,asset,start,end) for r in reviews):
                    raise ValueError("Scope already reviewed")
                reviews.append({
                    "address": address,"asset": asset,"start": start,"end": end,
                    "notes": notes,"status": "REVIEWED_NOT_VERIFIED",
                    "publication_approved": False
                })
                save(REVIEWS, reviews)
                return self.respond(200, {"message": "Scope review saved. No public changes."})
        except (ValueError, KeyError, TypeError, InvalidOperation) as exc:
            self.respond(400, {"error": str(exc)})

if __name__ == "__main__":
    print("Binance 14 Research Workspace: http://127.0.0.1:8767/", flush=True)
    print("Research data only · No public deployment", flush=True)
    ThreadingHTTPServer(("127.0.0.1", 8767), Handler).serve_forever()
