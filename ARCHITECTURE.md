# Architecture

This document is the recruiter- and reviewer-facing architecture summary for **Recon Engine** v1.0.0.

For pipeline-level detail, see also:

- [docs/architecture.md](docs/architecture.md)
- [docs/discovery-pipeline.md](docs/discovery-pipeline.md)
- [docs/evidence-pipeline.md](docs/evidence-pipeline.md)
- [docs/reporting-pipeline.md](docs/reporting-pipeline.md)
- [docs/engineering-decisions.md](docs/engineering-decisions.md)

---

## System context

```text
Operator (authorized lab / assessment)
        │
        ▼
   CLI / python -m recon
        │
        ▼
   ConfigLoader (CLI → YAML → assignment)
        │
        ▼
   ReconEngine
        ├── DiscoveryOrchestrator  → Normalizer
        ├── EvidenceOrchestrator   → artifact pack + SHA-256
        └── ReportingOrchestrator  → attack-surface PDF
```

External tools are invoked only through adapters:

| Adapter domain | Tools |
|----------------|-------|
| DNS | `dig` |
| HTTP | `curl` |
| Services | `nmap` |
| TLS | `openssl` |
| Line protocol / vhost / fingerprint | dedicated adapters |

---

## Layered design

| Layer | Package | Responsibility |
|-------|---------|----------------|
| Entry | `recon.__main__` | Argument parsing and engine invocation |
| Coordination | `recon.engine` | Ordered discovery → evidence → reporting |
| Configuration | `recon.configuration` | Assignment/YAML merge, scope, environment, output paths |
| Integration | `recon.adapters` | Subprocess boundaries around system tools |
| Domain | `recon.discovery` | Stage modules + normalization |
| Evidence | `recon.evidence` | Artifact writers + integrity |
| Presentation | `recon.reporting` | Narrative sections + PDF |

---

## Discovery sequence

```text
DNS → Probe → Service → TLS → Line Protocol → Virtual Host
  → Authentication → Authenticated HTTP → Fingerprint → Normalize
```

Later stages intentionally consume earlier results (for example, authentication after virtual-host discovery). The order is part of the assessment contract and should not be casually reordered.

---

## Evidence and integrity

Evidence writers emit a fixed artifact set under the configured output directory (default `output/`). `ManifestWriter` executes **last** so `manifest.sha256` covers the completed pack.

```text
normalized.json
scope-register.csv
request-ledger.csv
evidence-index.csv
assessment-manifest.json
continuity-record.md
integrity-attestation.md
foothold-evidence.txt
manifest.sha256          ← hashed last
attack-surface-report.pdf
```

Optional intermediate stage dumps may appear under `output/raw-output/`.

---

## Trust boundaries

1. **Authorization** — Operators must supply authorized targets/assignments; the project documents authorized-use constraints.
2. **Tool isolation** — Adapters own subprocess interaction.
3. **Schema stability** — Normalization isolates writers from raw tool quirks.
4. **Integrity** — Hash manifests support post-run verification.

---

## Extension model

Safe extension patterns are documented in [docs/extension-guide.md](docs/extension-guide.md):

- Add adapters without changing orchestrator contracts
- Register new discovery stages carefully (schema + docs + tests)
- Add evidence writers **before** the manifest writer
- Keep report sections pure functions of normalized data

---

## Quality attributes

| Attribute | Approach |
|-----------|----------|
| Reproducibility | Fixed stage order and stable filenames |
| Maintainability | Thin adapters; focused writers |
| Reviewability | Evidence-first artifacts |
| Safety | Scope-aware configuration and authorized-use documentation |
| Testability | Unit tests around normalizer and selected writers |

---

## Non-goals

- Dynamic plugin marketplace (future roadmap item)
- Pure-Python replacements for `nmap` / `openssl` in v1.0.0
- Exploitation or post-exploitation tooling
