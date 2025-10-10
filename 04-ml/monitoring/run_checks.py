import json, time, sys, pathlib

BASE = pathlib.Path(__file__).parent
BL = json.loads((BASE / "baseline.json").read_text())

# Simulated current metrics (in real life, compute from eval run outputs)
current = {
    "precision": 0.86,
    "recall":    0.78,
    "latency_ms": 420,
    "keyword_rate": 0.48   # simulate drift on keyword hits
}

# thresholds
fails = []
if current["precision"] < 0.80:  fails.append("precision<0.80")
if current["recall"]    < 0.75:  fails.append("recall<0.75")
if current["latency_ms"] > 1000: fails.append("latency>1000ms")

# drift check on keyword rate
delta = abs(current["keyword_rate"] - BL["keyword_rate"])
if delta > 0.10:
    fails.append(f"keyword_rate drift {delta:.2f} > 0.10")

# append run log
row = {
    "ts": int(time.time()),
    "precision": current["precision"],
    "recall": current["recall"],
    "latency_ms": current["latency_ms"],
    "keyword_rate": current["keyword_rate"],
    "keyword_rate_delta": round(current["keyword_rate"] - BL["keyword_rate"], 4),
    "status": "fail" if fails else "pass",
    "fails": fails
}
out = BASE / "metrics.jsonl"
with out.open("a") as f:
    f.write(json.dumps(row) + "\n")

# print a compact summary for CI logs
print("SUMMARY:", json.dumps(row))
sys.exit(1 if fails else 0)
