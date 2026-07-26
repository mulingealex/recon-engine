# Release Notes — Recon Engine v1.0.0

**Release date:** 2026-07-26  
**Repository:** [github.com/mulingealex/recon-engine](https://github.com/mulingealex/recon-engine)  
**License:** MIT  
**Author:** Alex M. Mulinge

---

## Summary

v1.0.0 marks the first public portfolio release of Recon Engine: a deterministic, scope-aware reconnaissance platform that produces integrity-preserving assessment evidence and an attack-surface report for authorized targets.

This release packages a completed assessment-grade engine with open-source documentation, community files, examples, and CI scaffolding—without changing the underlying reconnaissance pipeline semantics.

---

## Highlights

- End-to-end discovery pipeline from DNS through technology fingerprinting
- Normalization into a stable schema for downstream consumers
- Evidence pack generation with SHA-256 integrity manifest
- Attack-surface PDF reporting
- CLI entrypoint with assignment JSON and optional YAML configuration
- Unit tests for the normalizer and selected evidence writers
- Professional documentation and open-source repository layout

---

## Included capabilities

### Discovery

DNS, HTTP probe, service enumeration, TLS inspection, line-protocol discovery, virtual-host discovery, authentication discovery, authenticated HTTP discovery, and HTTP technology fingerprinting.

### Evidence

`normalized.json`, `scope-register.csv`, `request-ledger.csv`, `evidence-index.csv`, `assessment-manifest.json`, `continuity-record.md`, `integrity-attestation.md`, `foothold-evidence.txt`, and `manifest.sha256`.

### Reporting

Executive summary, findings, recommendations, appendix, and PDF assembly (`attack-surface-report.pdf`).

---

## Installation

```bash
git clone https://github.com/mulingealex/recon-engine.git
cd recon-engine
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

---

## Verify the release

```bash
python -m compileall src
pytest tests/unit -v
```

---

## Compatibility

| Item | Value |
|------|-------|
| Python | 3.13+ |
| Platform | Kali Linux / POSIX with dig, curl, nmap, OpenSSL |
| Package version | 1.0.0 |

---

## Security and authorized use

Recon Engine is intended only for systems you own or are explicitly authorized to assess. Report vulnerabilities privately per [SECURITY.md](SECURITY.md).

---

## Documentation map

| Document | Audience |
|----------|----------|
| [README.md](README.md) | Operators and GitHub visitors |
| [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) | Recruiters and hiring managers |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Engineers reviewing design |
| [CHANGELOG.md](CHANGELOG.md) | Change history |
| [ROADMAP.md](ROADMAP.md) | Planned work |
| [docs/](docs/) | Deep technical guides |

---

## Known limitations in v1.0.0

- Depends on local system tooling rather than a pure-Python network stack
- Portfolio screenshot PNGs are documented but not fabricated for this release
- Integration and acceptance test suites are reserved for future expansion

---

## Upgrade notes

v1.0.0 is the initial public semver tag for the portfolio release line. Operators upgrading from private assessment checkouts should continue using the same CLI and artifact filenames; no intentional output-contract break is introduced by documentation packaging.
