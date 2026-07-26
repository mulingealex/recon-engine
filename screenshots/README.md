# Screenshots

This directory stores **portfolio screenshots** referenced by the root [README.md](../README.md).

## Policy

- Do **not** invent or fabricate screenshots.
- Capture images only from **authorized** local lab runs.
- Prefer anonymized hosts (for example `127.0.0.1`) and redact secrets, tokens, and engagement identifiers.
- Commit PNGs only after real captures exist.

Until PNG files are present, the README **does not embed broken image links**. It lists planned filenames and shows the Markdown to add after capture.

---

## Exact captures required

| Filename | Resolution guidance | What to show |
|----------|---------------------|--------------|
| `cli-execution.png` | Terminal window, readable font | Engine run completing `[1/3] discovery`, `[2/3] evidence`, `[3/3] report` |
| `evidence-artifacts.png` | File tree or `ls` listing | `output/` contents including manifest, normalized JSON, and report PDF |
| `normalized-json.png` | Editor or `less`/`jq` view | Representative fields from `normalized.json` (probe/services/fingerprint) |
| `attack-surface-report.png` | PDF first page or viewer chrome cropped | `attack-surface-report.pdf` title/summary page |
| `manifest-sha256.png` | Terminal or editor | `manifest.sha256` contents or successful `sha256sum -c` / `examples/verify_manifest.sh` |

Optional extras (not required for README gallery):

| Filename | Purpose |
|----------|---------|
| `foothold-evidence.png` | Authenticated foothold proof when obtained |
| `raw-output-tree.png` | `output/raw-output/` stage dumps |

---

## Where each image belongs in the README

After files exist under `screenshots/`, embed them in [README.md](../README.md) under **Screenshots** (and optionally near related sections):

| File | Primary README section | Optional secondary placement |
|------|------------------------|------------------------------|
| `cli-execution.png` | Screenshots | Example Execution |
| `evidence-artifacts.png` | Screenshots | Example Output |
| `normalized-json.png` | Screenshots | Example Output (below JSON excerpt) |
| `attack-surface-report.png` | Screenshots | Evidence Generation |
| `manifest-sha256.png` | Screenshots | Evidence Generation |

### Markdown to paste into README (after PNGs exist)

From the repository root, embed images like this:

```text
![CLI execution](screenshots/cli-execution.png)
![Evidence artifacts](screenshots/evidence-artifacts.png)
![Normalized JSON](screenshots/normalized-json.png)
![Attack surface report](screenshots/attack-surface-report.png)
![Manifest verification](screenshots/manifest-sha256.png)
```

Paths are root-relative (`screenshots/...`), not relative to this file.

---

## Capture checklist

1. Run against an **authorized** lab target or assignment.
2. Confirm artifacts exist under `output/`.
3. Capture the five required PNGs using the filenames above (exact names).
4. Visually review for secrets before committing.
5. Update README Screenshots section to embed the images.
6. Open the GitHub README preview and confirm images render.

---

## Status

| File | Status |
|------|--------|
| `cli-execution.png` | Not captured yet |
| `evidence-artifacts.png` | Not captured yet |
| `normalized-json.png` | Not captured yet |
| `attack-surface-report.png` | Not captured yet |
| `manifest-sha256.png` | Not captured yet |
