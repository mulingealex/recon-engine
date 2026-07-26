# Architecture

## Purpose

Recon Engine is a modular reconnaissance platform that executes an ordered discovery pipeline against authorized targets, normalizes results, generates integrity-preserving evidence, and produces an assessment report.

This document describes the **logical architecture**. Runtime behavior of discovery, evidence, and reporting modules is intentionally unchanged by portfolio packaging work.

## High-Level Components

```text
CLI / __main__
      │
      ▼
ConfigLoader ──► ReconEngine
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
 Discovery     Evidence      Reporting
 Orchestrator  Orchestrator  Orchestrator
        │           │           │
   Adapters     Writers      Writers/PDF
```

| Component | Location | Role |
|-----------|----------|------|
| Entry point | `src/recon/__main__.py` | Parse args, load config, run engine |
| Engine | `src/recon/engine/` | Sequence discovery → evidence → reporting |
| Configuration | `src/recon/configuration/` | CLI, YAML, assignment JSON, scope, environment |
| Adapters | `src/recon/adapters/` | External tool wrappers |
| Discovery | `src/recon/discovery/` | Stage modules + normalizer |
| Evidence | `src/recon/evidence/` | Artifact writers + hashing |
| Reporting | `src/recon/reporting/` | Report sections + PDF |

## Data Flow

1. **Ingress** — Operator supplies a `target` and/or `--assignment` (and optional `--config`).
2. **Configuration merge** — `ConfigLoader` applies CLI → YAML → assignment precedence and normalizes host/port fields.
3. **Discovery** — `DiscoveryOrchestrator` runs modules in fixed order and optionally persists raw stage JSON.
4. **Normalization** — `Normalizer` projects stage results into a stable section schema.
5. **Evidence** — `EvidenceOrchestrator` writes CSV/JSON/Markdown artifacts; `ManifestWriter` hashes last.
6. **Reporting** — `ReportingOrchestrator` builds sections and emits `attack-surface-report.pdf`.
7. **Egress** — Engine returns artifact paths for operator confirmation.

## Discovery Module Graph

```text
DNSDiscovery
ProbeDiscovery
ServiceDiscovery
TLSDiscovery
LineProtocolDiscovery
VirtualHostDiscovery          ← consumes line protocol
AuthenticationDiscovery       ← consumes vhost + line protocol
AuthenticatedHTTPDiscovery    ← consumes authentication
FingerprintDiscovery          ← consumes virtual hosts
Normalizer
```

## Evidence Artifact Graph

Writers are ordered so integrity hashing observes a complete artifact set:

```text
NormalizedWriter
ScopeRegisterWriter
RequestLedgerWriter
EvidenceIndexWriter
AssessmentManifestWriter
ContinuityWriter
IntegrityWriter
FootholdEvidenceWriter
ManifestWriter                 ← SHA-256 last
```

## Reporting Artifact Graph

```text
ExecutiveSummaryWriter
FindingsWriter
RecommendationsWriter
AppendixWriter
PDFGenerator  →  output/attack-surface-report.pdf
```

## Trust and Safety Boundaries

- **Scope** — Configuration and validators gate assessment to authorized targets.
- **Tooling** — Adapters isolate subprocess interaction with system utilities.
- **Integrity** — Manifest hashing supports post-run verification of the evidence pack.
- **Authorization** — Operators remain responsible for legal authorization; the engine does not expand scope automatically.

## Extension Points

See [extension-guide.md](extension-guide.md) for adding adapters or discovery stages without breaking the public orchestrator contracts.

## Related Documents

- [Module overview](module-overview.md)
- [Discovery pipeline](discovery-pipeline.md)
- [Evidence pipeline](evidence-pipeline.md)
- [Reporting pipeline](reporting-pipeline.md)
- [Engineering decisions](engineering-decisions.md)
