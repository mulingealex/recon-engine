# Roadmap

Tracked against [github.com/mulingealex/recon-engine](https://github.com/mulingealex/recon-engine).

## Near Term

- [ ] Capture real portfolio screenshots after authorized demo runs ([screenshots/README.md](screenshots/README.md))
- [ ] Expand unit coverage for adapters with mocked subprocess boundaries
- [ ] Add integration tests against a disposable local lab profile
- [ ] Publish a short “how reviewers verify evidence” checklist

## Medium Term

- [ ] Optional HTML report companion to the PDF
- [ ] Richer TLS analytics (cipher suites, expiry warnings)
- [ ] Pluggable discovery module registration (backwards compatible)
- [ ] Containerized demo environment for recruiters

## Longer Term

- [ ] Signed evidence packs (beyond SHA-256 file lists)
- [ ] Multi-target batch mode with per-target isolation
- [ ] Structured logging / operator telemetry hooks
- [ ] Optional SARIF export for findings

## Non-Goals (Current)

- Exploitation / post-exploitation frameworks
- Unauthorized scanning features
- Breaking changes to assessed artifact filenames without a major version bump

Suggestions welcome via issues—see [CONTRIBUTING.md](CONTRIBUTING.md).
