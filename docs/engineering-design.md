# Engineering Design

This file is retained for continuity with earlier project documentation paths.

**Canonical design decision log:** [engineering-decisions.md](engineering-decisions.md)

**Canonical architecture:** [architecture.md](architecture.md)

## Design Summary

Recon Engine separates concerns into configuration, adapters, discovery, evidence, and reporting. A top-level engine orchestrates three subsystem orchestrators. Discovery results are normalized once, then consumed by evidence writers and report generators. Integrity hashing runs last so the evidence pack can be verified after the assessment completes.

## Quality Attributes

| Attribute | Approach |
|-----------|----------|
| Reproducibility | Fixed stage order and stable output filenames |
| Integrity | SHA-256 manifest over generated artifacts |
| Maintainability | Thin adapters and focused writers |
| Safety | Scope-aware configuration and authorized-use documentation |
| Extensibility | Documented extension points without breaking public package names |
