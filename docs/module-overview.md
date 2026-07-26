# Module Overview

## Package: `recon`

Top-level package for the reconnaissance engine. Primary entrypoint:

```bash
PYTHONPATH=src python -m recon [options]
```

| Subpackage | Description |
|------------|-------------|
| `recon.engine` | Workflow coordinator (`ReconEngine`) |
| `recon.configuration` | CLI, config loading, scope, environment, output paths |
| `recon.adapters` | External tool adapters |
| `recon.discovery` | Discovery modules + normalizer + orchestrator |
| `recon.evidence` | Evidence writers + orchestrator |
| `recon.reporting` | Report writers + PDF generator + orchestrator |

---

## `recon.engine`

| Module | Symbol | Role |
|--------|--------|------|
| `recon_engine.py` | `ReconEngine` | Runs discovery → evidence → reporting |

---

## `recon.configuration`

| Module | Symbol | Role |
|--------|--------|------|
| `cli_parser.py` | `CLIParser` | Argument definitions and validation |
| `config_loader.py` | `ConfigLoader` | Merge CLI / YAML / assignment |
| `environment_checker.py` | `EnvironmentChecker` | Tooling / environment checks |
| `output_manager.py` | `OutputManager` | Output path management |
| `scope_validator.py` | `ScopeValidator` | Scope safety checks |

---

## `recon.adapters`

| Module | Symbol | Tool |
|--------|--------|------|
| `dig_adapter.py` | `DigAdapter` | `dig` |
| `curl_adapter.py` | `CurlAdapter` | `curl` |
| `nmap_adapter.py` | `NmapAdapter` | `nmap` |
| `openssl_adapter.py` | `OpenSSLAdapter` | `openssl` |
| `line_protocol_adapter.py` | `LineProtocolAdapter` | Line protocol probes |
| `vhost_adapter.py` | `VHostAdapter` | Virtual host probes |
| `fingerprint_adapter.py` | `FingerprintAdapter` | HTTP fingerprinting |

---

## `recon.discovery`

| Module | Symbol | Stage |
|--------|--------|-------|
| `dns_discovery.py` | `DNSDiscovery` | DNS |
| `probe_discovery.py` | `ProbeDiscovery` | HTTP probe |
| `service_discovery.py` | `ServiceDiscovery` | Services |
| `tls_discovery.py` | `TLSDiscovery` | TLS |
| `line_protocol_discovery.py` | `LineProtocolDiscovery` | Line protocol |
| `virtual_host_discovery.py` | `VirtualHostDiscovery` | Virtual hosts |
| `authentication_discovery.py` | `AuthenticationDiscovery` | Authentication |
| `authenticated_http_discovery.py` | `AuthenticatedHTTPDiscovery` | Authenticated HTTP |
| `fingerprint_discovery.py` | `FingerprintDiscovery` | Fingerprinting |
| `normalizer.py` | `Normalizer` | Schema normalization |
| `orchestrator.py` | `DiscoveryOrchestrator` | Stage coordination |

---

## `recon.evidence`

| Module | Symbol | Artifact |
|--------|--------|----------|
| `normalized_writer.py` | `NormalizedWriter` | `normalized.json` |
| `scope_register_writer.py` | `ScopeRegisterWriter` | `scope-register.csv` |
| `request_ledger_writer.py` | `RequestLedgerWriter` | `request-ledger.csv` |
| `evidence_index_writer.py` | `EvidenceIndexWriter` | `evidence-index.csv` |
| `assessment_manifest_writer.py` | `AssessmentManifestWriter` | `assessment-manifest.json` |
| `continuity_writer.py` | `ContinuityWriter` | `continuity-record.md` |
| `integrity_writer.py` | `IntegrityWriter` | `integrity-attestation.md` |
| `foothold_evidence_writer.py` | `FootholdEvidenceWriter` | `foothold-evidence.txt` |
| `manifest_writer.py` | `ManifestWriter` | `manifest.sha256` |
| `raw_output_writer.py` | `RawOutputWriter` | `raw-output/*.json` |
| `orchestrator.py` | `EvidenceOrchestrator` | Writer coordination |

---

## `recon.reporting`

| Module | Symbol | Role |
|--------|--------|------|
| `executive_summary_writer.py` | `ExecutiveSummaryWriter` | Executive summary section |
| `findings_writer.py` | `FindingsWriter` | Findings section |
| `recommendations_writer.py` | `RecommendationsWriter` | Recommendations section |
| `appendix_writer.py` | `AppendixWriter` | Appendix section |
| `pdf_generator.py` | `PDFGenerator` | PDF assembly |
| `orchestrator.py` | `ReportingOrchestrator` | Report coordination |

---

## Tests

| Path | Focus |
|------|-------|
| `tests/unit/` | Normalizer and selected evidence writers |
| `tests/integration/` | Reserved for end-to-end paths |
| `tests/acceptance/` | Reserved for acceptance criteria |

Public exports for each package are declared in the corresponding `__init__.py` `__all__` lists.
