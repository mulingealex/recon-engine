# Recon Engine

## Overview

Recon Engine is a modular reconnaissance platform developed for the UBI Advanced Ethical Hacking Project (Stage 5).

The platform performs scope-aware reconnaissance against authorized targets while maintaining evidence integrity and reproducibility. It automates multiple reconnaissance phases and generates structured artifacts suitable for technical assessment and evidence review.

---

## Features

- DNS discovery
- HTTP probing
- Service enumeration
- TLS inspection
- Line protocol discovery
- Virtual host enumeration
- Authentication discovery
- Authenticated HTTP discovery
- HTTP technology fingerprinting
- Evidence generation
- Scope registration
- Request ledger generation
- Assessment reporting

---

## Project Architecture

```
Recon Engine
│
├── Discovery Modules
│   ├── DNS
│   ├── Probe
│   ├── Service
│   ├── TLS
│   ├── Line Protocol
│   ├── Virtual Host
│   ├── Authentication
│   ├── Authenticated HTTP
│   └── Fingerprinting
│
├── Normalization
│
├── Reporting
│
└── Evidence Generation
```

---

## Technology Stack

- Python 3.13
- Kali Linux
- curl
- dig
- nmap
- openssl

---

## Repository Structure

```
src/
tests/
resources/
scripts/
docs/
output/
```

---

## Requirements

- Python 3.13+
- curl
- dig
- nmap
- openssl

---

## Installation

```bash
python -m venv .venv

source .venv/bin/activate

pip install -e .
```

---

## Running the Engine

```bash
PYTHONPATH=src python -m recon \
    --assignment ../stage5-lab/lab-runtime/assignment.json
```

---

## Generated Artifacts

Running the engine generates evidence under the `output/` directory, including:

- normalized.json
- scope-register.csv
- request-ledger.csv
- attack-surface-report.pdf
- evidence-index.csv
- assessment-manifest.json
- integrity-attestation.md
- manifest.sha256
- continuity-record.md

---

## Testing

Execute the automated test suite:

```bash
pytest
```

If XML reporting is required:

```bash
pytest --junitxml=test-results.xml
```

---

## Operating Environment

Operating System:
Kali Linux

Python:
3.13

---

## Assessment Variant

Advanced Project 1 – Stage 5

---

## Evidence Marker

Evidence is generated automatically within the `output/` directory and is referenced through:

- normalized.json
- request-ledger.csv
- evidence-index.csv

---

## Reproduction Procedure

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install project dependencies.
4. Launch the Stage 5 runtime.
5. Execute the Recon Engine.
6. Review generated evidence under `output/`.
7. Verify integrity using `manifest.sha256`.

---

