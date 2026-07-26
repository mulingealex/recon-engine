# Extension Guide

## Goals

Extend Recon Engine without breaking assessment contracts:

- Preserve discovery order unless intentionally redesigned
- Keep normalized schema keys stable or version them deliberately
- Avoid changing existing evidence/report semantics in place

## Adding an Adapter

1. Create `src/recon/adapters/<tool>_adapter.py` with a focused class.
2. Encapsulate subprocess invocation and return structured `dict` data.
3. Export the class from `src/recon/adapters/__init__.py`.
4. Consume the adapter from a discovery module—not from the engine directly.

## Adding a Discovery Stage

1. Implement `src/recon/discovery/<name>_discovery.py` with an `execute(...)` method.
2. Wire the stage into `DiscoveryOrchestrator` at the correct dependency point.
3. Add the stage key to the orchestrator aggregation dict.
4. Extend `Normalizer` only if a new top-level schema section is required.
5. Update docs: `discovery-pipeline.md`, `module-overview.md`, and tests.

## Adding an Evidence Writer

1. Implement a writer with a `write(normalized_data: dict) -> dict` style contract matching siblings.
2. Register it in `EvidenceOrchestrator` **before** `ManifestWriter`.
3. Document the artifact in `evidence-pipeline.md` and the README evidence table.
4. Add unit coverage for deterministic output shape when practical.

## Adding a Report Section

1. Add a section writer under `src/recon/reporting/`.
2. Invoke it from `ReportingOrchestrator` before PDF generation.
3. Keep section writers pure functions of normalized data.

## Compatibility Checklist

- [ ] Existing unit tests still pass
- [ ] Normalized keys used by current writers remain present
- [ ] Manifest still hashes the complete evidence set
- [ ] README / docs updated for operator-visible changes
- [ ] No secrets committed in examples or fixtures

## What Not To Do

- Do not scrape credentials into the repository
- Do not target unauthorized hosts in examples or CI
- Do not silently reorder discovery stages
- Do not change hash algorithm or artifact filenames without a changelog entry

## Related Documents

- [Engineering decisions](engineering-decisions.md)
- [Developer guide](developer-guide.md)
- [Contributing](../CONTRIBUTING.md)
