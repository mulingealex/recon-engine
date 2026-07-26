# Engineering Decisions

## Context

Recon Engine was developed as a Stage 5 ethical hacking / VAPT assessment project and is maintained as a portfolio-grade open-source codebase. The following decisions explain *why* the system is structured the way it is.

## Decision Log

### 1. Orchestrator pattern per subsystem

**Decision:** Separate orchestrators for discovery, evidence, and reporting.

**Rationale:** Each subsystem has a different lifecycle (network I/O vs filesystem writes vs document assembly). Independent orchestrators keep failure domains and testing surfaces small.

**Consequence:** Adding a discovery module does not require changing evidence writers, and vice versa—only the parent `ReconEngine` sequence remains shared.

### 2. Adapter boundary around system tools

**Decision:** Wrap `dig`, `curl`, `nmap`, and `openssl` in adapter classes.

**Rationale:** Keeps subprocess details out of discovery modules, improves readability, and allows future mocking in tests without rewriting assessment logic.

**Consequence:** Discovery code speaks in Python data structures; adapters own command construction and output capture.

### 3. Fixed discovery order

**Decision:** Execute discovery stages in a deterministic sequence rather than a dynamic graph engine.

**Rationale:** Assessment reproducibility and auditability outweigh dynamic scheduling for this problem size. Later stages intentionally consume earlier results (for example, authentication after virtual hosts).

**Consequence:** Pipeline behavior is predictable and easy to document; reordering stages is a deliberate engineering change, not an operator toggle.

### 4. Normalize before evidence and reporting

**Decision:** A dedicated `Normalizer` produces a stable schema consumed by all writers.

**Rationale:** Prevents CSV/PDF writers from depending on raw tool quirks. Missing sections become empty dictionaries instead of KeyErrors.

**Consequence:** Schema evolution happens in one place; writers remain thin.

### 5. Hash artifacts last

**Decision:** `ManifestWriter` executes after other evidence writers.

**Rationale:** Integrity attestation must cover the final evidence pack, not a partial write set.

**Consequence:** Manifest regeneration is required if any prior artifact is modified after hashing.

### 6. Assignment JSON for lab runtimes

**Decision:** Support `--assignment` for educational lab profiles in addition to direct targets.

**Rationale:** Aligns with Stage 5 runtime packaging while preserving a simple direct-target CLI for demos.

**Consequence:** Configuration loading must merge multiple sources with clear precedence (CLI → YAML → assignment).

### 7. Evidence-first operator experience

**Decision:** Treat filesystem artifacts as first-class deliverables, not optional logs.

**Rationale:** Security assessments require chain-of-custody, reproducibility, and reviewer-friendly evidence—not only console output.

**Consequence:** Output layout is part of the product contract; documentation emphasizes artifact semantics.

### 8. Presentation changes without behavior changes

**Decision:** Portfolio/open-source hardening (README, docs, CI templates, metadata) must not alter discovery logic, normalization, evidence content, or report generation.

**Rationale:** The project has already been assessed; behavioral drift would invalidate prior verification.

**Consequence:** Contributions that change engine semantics require explicit review beyond documentation PRs.

## Non-Goals

- Replacing commercial attack-surface management platforms
- Implementing exploit delivery or post-exploitation frameworks
- Pure-Python replacements for `nmap` / `openssl` in this version

## Related Documents

- [Architecture](architecture.md)
- [Developer guide](developer-guide.md)
- [Roadmap](../ROADMAP.md)
