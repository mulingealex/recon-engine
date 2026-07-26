# Examples

Realistic operator recipes for **authorized** lab use only.

| Example | Description |
|---------|-------------|
| [`sample_assignment.json`](sample_assignment.json) | Illustrative assignment document (not a live lab secret pack) |
| [`run_with_assignment.sh`](run_with_assignment.sh) | Run via `--assignment` |
| [`run_direct_target.sh`](run_direct_target.sh) | Run against a local authorized target |
| [`verify_manifest.sh`](verify_manifest.sh) | Recompute hashes and compare to `manifest.sha256` |

## Safety

- Replace hosts/ports with values from **your** authorized assignment.
- Do not commit real credentials, tokens, or engagement data.
- Prefer disposable lab networks.

## Quick demo

```bash
# From repository root, with venv active
chmod +x examples/*.sh
./examples/run_with_assignment.sh
```
