# Project Overview

**Recon Engine** is a modular, evidence-first reconnaissance platform for **authorized** cybersecurity assessments.

| | |
|---|---|
| **Author** | Alex M. Mulinge |
| **Repository** | [github.com/mulingealex/recon-engine](https://github.com/mulingealex/recon-engine) |
| **Language** | Python 3.13 |
| **License** | MIT |
| **Version** | 1.0.0 |
| **Primary audience** | Security engineers, VAPT practitioners, hiring managers reviewing portfolio work |

---

## What it does

Given an authorized target (or lab assignment), the engine:

1. Runs a fixed discovery pipeline (DNS → probe → services → TLS → line protocol → virtual hosts → authentication → authenticated HTTP → fingerprinting)
2. Normalizes results into a stable schema
3. Writes a verifiable evidence pack (JSON/CSV/Markdown + SHA-256 manifest)
4. Produces an attack-surface PDF report

Operators get reviewer-ready artifacts instead of unstructured shell logs.

---

## Why this project matters (hiring signal)

| Signal | Evidence in the repo |
|--------|----------------------|
| Systems thinking | Clear separation of adapters, discovery, evidence, and reporting |
| Security craft | Scope-aware operation, integrity hashing, continuity/attestation artifacts |
| Software engineering | Typed package layout, orchestrators, unit tests, `pyproject.toml` packaging |
| Professional communication | Architecture docs, examples, security policy, contribution guidelines |
| Operational realism | Uses real Kali tools (`dig`, `curl`, `nmap`, `openssl`) behind adapters |

---

## Quick evaluation path (10 minutes)

1. Read this file and [ARCHITECTURE.md](ARCHITECTURE.md)
2. Skim [README.md](README.md) feature and evidence tables
3. Open `src/recon/engine/recon_engine.py` and `src/recon/discovery/orchestrator.py`
4. Run `pytest tests/unit -v` after `pip install -e ".[dev]"`
5. Review `examples/` for operator usage patterns

---

## Design highlights

- **Deterministic pipeline** — stage order is explicit and documented
- **Normalize once** — writers and reporting consume one schema
- **Hash last** — integrity manifest covers the completed evidence pack
- **Authorized-use posture** — documented constraints; not a mass-scanning product

---

## What this is not

- Not a commercial attack-surface management platform
- Not an exploitation or post-exploitation framework
- Not intended for unauthorized scanning

---

## Related documents

| Document | Purpose |
|----------|---------|
| [README.md](README.md) | Operator landing page |
| [ARCHITECTURE.md](ARCHITECTURE.md) | Architecture summary |
| [RELEASE_NOTES_v1.0.0.md](RELEASE_NOTES_v1.0.0.md) | v1.0.0 release summary |
| [docs/](docs/) | Deep technical documentation |
| [ROADMAP.md](ROADMAP.md) | Planned improvements |
| [SECURITY.md](SECURITY.md) | Vulnerability reporting |

---

## Contact

- GitHub: [mulingealex](https://github.com/mulingealex)
- LinkedIn: [Alex Mulinge](https://www.linkedin.com/in/alex-mulinge-448708361)
- Email: mulingealex68@gmail.com
