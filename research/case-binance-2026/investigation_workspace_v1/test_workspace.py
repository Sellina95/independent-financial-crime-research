import hashlib
import importlib.util
import json
import re
import tempfile
import threading
import urllib.error
import urllib.request
from http.server import ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APP = ROOT / "research_app.py"

spec = importlib.util.spec_from_file_location("research_under_test", APP)
app = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app)

protected = [app.BASE, app.DRAFT, app.REVIEWS]
before = {
    str(p): hashlib.sha256(p.read_bytes()).hexdigest()
    for p in protected
}

EXPECTED_SHA = (
    "a3897b5a3896c3ada2ca57690ce3da4b430d"
    "de23eee9b169452814be70c59589"
)

SOURCE = "0x28c6c06298d514db089934071355e5743bf21d60"
TARGET = "0x" + "f" * 40
TX = "0x" + "9" * 64

try:
    assert hashlib.sha256(app.BASE.read_bytes()).hexdigest() == EXPECTED_SHA
    assert len(app.load(app.BASE)) == 1057
    assert app.load(app.DRAFT) == []
    assert app.load(app.REVIEWS) == []
    print("01 ORIGINAL EVIDENCE: PASS")

    known = (
        "0x0ef56ff332020a269cbb2fe1fc9619a"
        "35940682a60f9087a147fc9bffbf09857"
    )
    assert app.registration_status(
        known,
        SOURCE,
        "0xb5604684e5150a1935be954b0aee60db84d797ea",
        "USDT",
        "0xdac17f958d2ee523a2206206994597c13d831ec7",
        "29.408117",
        64
    ) == "REGISTERED"
    print("02 ERC20 EVENT IDENTITY: PASS")

    original = app.render_original_map()
    assert 'id="graph"' in original
    print("03 ORIGINAL GRAPH: PASS")

    with tempfile.TemporaryDirectory(prefix="binance26k_") as temp:
        temp = Path(temp)

        app.DRAFT = temp / "draft.json"
        app.REVIEWS = temp / "reviews.json"

        app.DRAFT.write_text("[]\n", encoding="utf-8")
        app.REVIEWS.write_text("[]\n", encoding="utf-8")

        server = ThreadingHTTPServer(
            ("127.0.0.1", 0), app.Handler
        )
        port = server.server_address[1]

        thread = threading.Thread(
            target=server.serve_forever,
            daemon=True
        )
        thread.start()

        def request(path, payload=None):
            data = None if payload is None else json.dumps(payload).encode()
            req = urllib.request.Request(
                f"http://127.0.0.1:{port}{path}",
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST" if payload is not None else "GET"
            )
            try:
                with urllib.request.urlopen(req, timeout=10) as response:
                    raw = response.read()
                    if path.startswith("/original-map"):
                        return response.status, raw.decode()
                    return response.status, json.loads(raw)
            except urllib.error.HTTPError as error:
                return error.code, json.loads(error.read())

        try:
            # Synthetic data exists ONLY in a temporary directory.
            fixture = {
                "tx": TX,
                "from": SOURCE,
                "to": TARGET,
                "block": "26310000",
                "utc": "2026-10-31T01:00:00",
                "asset": "ETH",
                "amount": "1.25",
                "contract": ""
            }

            status, result = request("/api/event", fixture)
            assert status == 200, result

            drafts = app.load(app.DRAFT)
            assert len(drafts) == 1
            assert drafts[0]["evidence_status"] == "DRAFT"
            assert drafts[0]["evidence_origin"] == "MANUAL_UNVERIFIED"
            assert drafts[0]["incident_attribution"] == "UNKNOWN"
            print("04 ISOLATED DRAFT SAVE: PASS")

            status, result = request("/api/event", fixture)
            assert status == 400, result
            assert len(app.load(app.DRAFT)) == 1
            print("05 DUPLICATE PROTECTION: PASS")

            status, data = request("/api/data")
            assert status == 200
            assert len(data["events"]) == 1058
            assert any(
                e["tx_hash"] == TX
                and e["status"] == "DRAFT"
                and e["evidence_origin"] == "MANUAL_UNVERIFIED"
                for e in data["events"]
            )
            print("06 TIMELINE DATA: PASS")

            status, html = request("/original-map")
            assert status == 200

            match = re.search(
                r'<script type="application/json" id="dataset">'
                r'(.*?)</script>',
                html, re.DOTALL
            )
            assert match

            graph = json.loads(match.group(1))
            assert len(graph["nodes"]) == 154
            assert len(graph["edges"]) == 1058
            assert any(
                e["tx_hash"] == TX
                and e["to_address"] == TARGET
                for e in graph["edges"]
            )
            print("07 GRAPH NODE + EDGE: PASS")

            assert not any(
                r.get("publication_approved")
                for r in app.load(app.REVIEWS)
            )
            print("08 NO PUBLICATION APPROVAL: PASS")

        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)

finally:
    after = {
        str(p): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in protected
    }
    assert before == after, "STOP: Actual research files changed"
    print("09 REAL RESEARCH FILE INTEGRITY: PASS")

print()
print("=== STEP 26K REGRESSION PASS ===")
print("SYNTHETIC DATA DISCARDED")
print("MAIN UNCHANGED · NO COMMIT · NO PUSH")
