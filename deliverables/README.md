# Deliverables

Use this directory for **curated assessment archives** you intentionally want tracked or shared.

## Guidance

- Runtime artifacts continue to land in `output/` (gitignored contents).
- **Do not delete** existing assessment evidence from your working tree.
- If you need a durable portfolio/submission copy, copy selected files here and document them in a short note (date, commit, lab profile).

Example (local only):

```bash
mkdir -p deliverables/stage5-run-2026-07-25
cp output/normalized.json \
   output/assessment-manifest.json \
   output/manifest.sha256 \
   output/attack-surface-report.pdf \
   deliverables/stage5-run-2026-07-25/
```

See [docs/artifact-policy.md](../docs/artifact-policy.md).
