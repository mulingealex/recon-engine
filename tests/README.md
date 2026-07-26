# Tests

| Suite | Path | Status |
|-------|------|--------|
| Unit | `tests/unit/` | Active |
| Integration | `tests/integration/` | Reserved |
| Acceptance | `tests/acceptance/` | Reserved |

```bash
PYTHONPATH=src pytest tests/unit -v
```

With `pyproject.toml` `pythonpath = ["src"]`, `pytest tests/unit -v` also works after editable install.
