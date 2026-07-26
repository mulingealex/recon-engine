# Implementation Plan — Portfolio Hardening

> Generated during the repository audit. Behavior of discovery, evidence, reporting, and tests remains frozen.

## Audit Findings

| Finding | Severity | Action |
|---------|----------|--------|
| Empty `docs/*.md` placeholders | High | Replace with full documentation suite |
| Assessment-oriented README | High | Rewrite as OSS/portfolio landing page |
| Missing LICENSE / community files | High | Add MIT + CONTRIBUTING/SECURITY/COC/CHANGELOG/ROADMAP |
| Missing `.github/` CI & templates | Medium | Add workflows, Dependabot, issue/PR templates |
| Missing `examples/` and `screenshots/` | Medium | Add realistic examples + screenshot placeholders |
| Weak `.gitignore` (egg-info, JUnit XML) | Medium | Expand ignore rules; document artifact policy |
| Empty package docstring / minor style gaps | Low | Improve headers, type hints, public API docs |
| Debug print in alternate engine `main()` | Low | Remove debug leftover (no discovery logic change) |
| `evidence-index-template(1).csv` naming | Low | Rename to professional filename |
| Empty `deliverables/`, `scripts/`, etc. | Low | Add README guidance files |

## Workstreams

1. **Documentation** — README + docs suite
2. **Repository organization** — OSS metadata and GitHub assets
3. **Developer experience** — examples, screenshots placeholders, ignore policy
4. **Code presentation** — docstrings/types/format only
5. **Recruiter review** — iterate presentation until portfolio-ready
6. **Final audit** — scorecard in `docs/portfolio-audit.md`

## Non-Goals

- Changing discovery / normalization / evidence / report logic
- Renaming Python packages
- Pushing to GitHub or creating remotes
- Deleting assessment evidence from disk
