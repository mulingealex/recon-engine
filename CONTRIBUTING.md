# Contributing to Recon Engine

Thank you for contributing. This project values clarity, safety, and backwards compatibility.

Repository: [github.com/mulingealex/recon-engine](https://github.com/mulingealex/recon-engine)

## Ground Rules

1. **Authorized use only** — Do not submit examples, fixtures, or CI jobs that target systems without authorization.
2. **Preserve engine contracts** — Discovery, normalization, evidence, and report generation logic must not change unless a change is explicitly scoped, reviewed, and tested.
3. **Be respectful** — Follow the [Code of Conduct](CODE_OF_CONDUCT.md).
4. **Prefer small PRs** — Documentation, tests, and DX improvements are especially welcome.

## Development Setup

See [docs/developer-guide.md](docs/developer-guide.md).

```bash
git clone https://github.com/mulingealex/recon-engine.git
cd recon-engine
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest tests/unit -v
```

## Branch and Commit Guidance

- Branch from `master` (default branch)
- Use clear commit messages focused on *why*
- Do not commit secrets, credentials, or live engagement data
- Do not commit runtime `output/` artifacts or `test-results.xml`

## Pull Requests

Use the PR template and include:

- Summary of the change
- Test plan
- Confirmation that discovery/evidence/report behavior is unchanged (when applicable)

## Security Issues

Report vulnerabilities privately via [SECURITY.md](SECURITY.md). Do not open public issues for security reports.

## License

By contributing, you agree that your contributions are licensed under the [MIT License](LICENSE).

## Questions

Open a documentation issue if something in the guides is unclear.
