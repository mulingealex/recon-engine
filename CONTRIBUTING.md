# Contributing to Recon Engine

Thank you for contributing. This project values clarity, safety, and backwards compatibility.

## Ground Rules

1. **Authorized use only** — Do not submit examples, fixtures, or CI jobs that target systems without authorization.
2. **No behavior drift in portfolio PRs** — Discovery, normalization, evidence, and report generation logic is assessment-frozen unless a change is explicitly scoped and reviewed.
3. **Be respectful** — Follow the [Code of Conduct](CODE_OF_CONDUCT.md).
4. **Prefer small PRs** — Documentation, tests, and DX improvements are especially welcome.

## Development Setup

See [docs/developer-guide.md](docs/developer-guide.md).

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
pip install pytest pyyaml
PYTHONPATH=src pytest tests/unit -v
```

## Branch & Commit Guidance

- Branch from `master` (or the default branch)
- Use clear commit messages focused on *why*
- Do not commit secrets, credentials, or live engagement data
- Do not commit runtime `output/` artifacts or `test-results.xml`

## Pull Requests

Use the PR template and include:

- Summary of the change
- Test plan
- Confirmation that discovery/evidence/report behavior is unchanged (when applicable)

## Security Issues

Report vulnerabilities privately via [SECURITY.md](SECURITY.md).

## Questions

Open a documentation issue or discussion if something in the guides is unclear.
