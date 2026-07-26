# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.0.x   | Yes       |
| 0.1.x   | Best effort (upgrade to 1.0.x recommended) |

## Authorized Use

Recon Engine is intended for **authorized** laboratory, educational, and professional assessments only. Misuse against systems without permission may be illegal.

Repository: [github.com/mulingealex/recon-engine](https://github.com/mulingealex/recon-engine)

## Reporting a Vulnerability

Please **do not** open a public GitHub issue for security vulnerabilities.

Instead, email **mulingealex68@gmail.com** with:

- A clear description of the issue
- Steps to reproduce
- Impact assessment (if known)
- Any suggested remediation

You should receive an acknowledgement within **7 days**. Coordinated disclosure is preferred.

## Scope Notes

In scope:

- Dependency supply-chain issues affecting this project
- Unsafe subprocess handling in adapters
- Path traversal or unsafe writes in artifact writers
- Secret leakage in examples, docs, or committed fixtures

Out of scope:

- Findings that require unauthorized scanning of third-party systems
- Theoretical issues without a practical impact path

Findings that would require changing assessed discovery logic will be triaged carefully to preserve assessment integrity while addressing risk.

## Safe Harbor

Good-faith security research against **this repository’s source code** (not third-party production targets) is welcome when conducted without violating applicable law or GitHub terms.

## Related

- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [LICENSE](LICENSE)
