PQC Baseline
Algorithms: Kyber for key encapsulation, Dilithium for signatures, SHA-3 or Blake3 for hash.
TLS: OQS OpenSSL hybrid ciphers with crypto agility enabled.
Data at rest: envelope encryption Kyber to AES GCM, signed manifests with Dilithium.
Keys: HSM or Vault, split custody, quarterly rotation, emergency revoke SOP.
Audit: append-only logs, daily hash anchoring.
