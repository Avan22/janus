PQC Baseline
Use Kyber for key encapsulation, Dilithium for signatures, SHA-3/Blake3 for hashing.
TLS via OQS-OpenSSL hybrids when available; maintain crypto-agility.
Data at rest: envelope encryption (symmetric key wrapped by Kyber); signed manifests with Dilithium.
Keys: stored in a local vault until HSM budget; quarterly rotation plan written; emergency revoke procedure documented.
Audit: append-only logs; daily hash anchoring to a public chain when budget permits.
