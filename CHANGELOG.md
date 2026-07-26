# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned

- Portfolio screenshot captures from authorized demo runs
- Expanded adapter unit coverage with mocked subprocess boundaries
- Integration tests against a disposable lab profile

## [1.0.0] - 2026-07-26

### Added

- Public portfolio release packaging for Recon Engine
- Professional README with badges, Mermaid workflow, and documentation links
- Root documents: `PROJECT_OVERVIEW.md`, `ARCHITECTURE.md`, `RELEASE_NOTES_v1.0.0.md`
- Documentation suite under `docs/` (architecture, pipelines, developer and extension guides)
- Community files: `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `ROADMAP.md`
- GitHub issue/PR templates, CI workflow, and Dependabot configuration
- `examples/` operator recipes and sample assignment
- Screenshot capture guide under `screenshots/`
- Artifact tracking policy documentation

### Changed

- Package metadata version set to `1.0.0`
- Repository URLs aligned to `https://github.com/mulingealex/recon-engine`
- Expanded `.gitignore` for packaging, test artifacts, and secrets
- Improved package/module documentation and type-hint presentation (no engine behavior changes)

## [0.1.0] - 2026-07-25

### Added

- End-to-end reconnaissance engine for Stage 5 assessment
- Discovery pipeline (DNS through fingerprinting)
- Evidence generation and integrity manifest
- Attack-surface PDF reporting
- Unit tests for normalizer and selected evidence writers
