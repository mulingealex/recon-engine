# Developer Guide

## Prerequisites

- Python 3.13+
- Kali Linux (or equivalent with `dig`, `curl`, `nmap`, `openssl`)
- Git

## Setup

```bash
git clone https://github.com/mulingealex/recon-engine.git
cd recon-engine
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

## Running Locally

```bash
PYTHONPATH=src python -m recon --assignment /path/to/assignment.json
# or
PYTHONPATH=src python -m recon 127.0.0.1 --output output
```

## Testing

```bash
PYTHONPATH=src pytest tests/unit -v
python -m compileall src
```

## Code Style

Configured in `pyproject.toml`:

- **Black** — line length 88, Python 3.13
- **Ruff** — lint target `py313`
- **mypy** — Python 3.13

Suggested local checks:

```bash
ruff check src tests
black --check src tests
```

## Project Conventions

- Prefer clear module headers and NumPy-style parameter docs where already used.
- Keep adapters thin; put sequencing in orchestrators.
- Do not change discovery, normalization, evidence, or report **behavior** in documentation-only or portfolio PRs.
- Keep public exports updated in package `__init__.py` `__all__` lists.

## Directory Expectations

| Path | Expectation |
|------|-------------|
| `src/recon/` | Production package |
| `tests/` | Automated tests |
| `docs/` | Architecture and guides |
| `examples/` | Operator recipes |
| `output/` | Runtime artifacts (contents gitignored) |
| `deliverables/` | Optional assessment archive copies |

## Debugging Tips

1. Inspect `output/raw-output/` for per-stage JSON (when written).
2. Compare `normalized.json` against stage dumps to isolate normalization vs discovery issues.
3. Confirm tool availability (`dig`, `curl`, `nmap`, `openssl`) before deep debugging.
4. Use a known lab assignment JSON for reproducible runs.

## Related Documents

- [Extension guide](extension-guide.md)
- [Architecture](architecture.md)
- [Contributing](../CONTRIBUTING.md)
