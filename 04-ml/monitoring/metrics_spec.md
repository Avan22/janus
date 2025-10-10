# ML Monitoring Spec (Phase 6)
Scope: basic quality + drift checks for demo artifacts.

Tracked signals (per run):
- quality/precision: float [0..1]
- quality/recall: float [0..1]
- latency_ms: float
- drift/keyword_rate_delta: float (abs delta vs. baseline keyword hit-rate)

Thresholds (fail the run if):
- precision < 0.80 OR recall < 0.75
- latency_ms > 1000
- abs(keyword_rate_delta) > 0.10

Storage:
- Append JSONL to 04-ml/monitoring/metrics.jsonl
- Keep baseline at 04-ml/monitoring/baseline.json

Owner:
- Name: Avaneendra Trivedi
- Email: avaneendra22@gmail.com
- Phone: +91-9098260879
- Address: residence of principal OPJS campus, raigarh, chhattisgarh, 496001, india
