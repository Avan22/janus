ML Security Policy
Scope: all notebooks, scripts, datasets, models.
Data rules: no raw PII; only minimum features; sanitize free text before saving; keep data in approved folders.
Access: least privilege; read-only for eval artifacts; write allowed only in feature engineering repos.
Secrets: never in notebooks; use env vars or local vault.
Models: store cards; record training data versions and licenses; keep signed hashes of model files.
Shipping gate: eval baseline must pass; fairness notes included where applicable; red-team prompts recorded for LLMs.
Incidents: rotate keys; quarantine artifacts; write postmortem under 00-admin/incidents/.
