# Reporting Pipeline

## Objective

Produce a human-readable attack-surface assessment report from normalized discovery data.

## Orchestrator

`ReportingOrchestrator` (`src/recon/reporting/orchestrator.py`) builds report sections, then hands content to `PDFGenerator`.

```text
Executive Summary
Findings
Recommendations
Appendix
        │
        ▼
   PDFGenerator
        │
        ▼
output/attack-surface-report.pdf
```

## Section Writers

| Writer | Responsibility |
|--------|----------------|
| `ExecutiveSummaryWriter` | High-level assessment narrative |
| `FindingsWriter` | Technical findings derived from normalized data |
| `RecommendationsWriter` | Remediation / hardening guidance |
| `AppendixWriter` | Supporting detail for reviewers |

## Output Contract

Primary deliverable:

```text
output/attack-surface-report.pdf
```

The engine surfaces the report path in the final artifact summary printed to the console.

## Design Constraints

- Reporting **consumes normalized data only**—it does not re-run discovery.
- Section writers remain independent so narrative quality can improve without changing discovery behavior.
- Portfolio packaging must not alter report generation semantics.

## Related Documents

- [Architecture](architecture.md)
- [Evidence pipeline](evidence-pipeline.md)
- [Engineering decisions](engineering-decisions.md)
