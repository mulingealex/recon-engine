#!/usr/bin/env bash
# Verify SHA-256 digests listed in output/manifest.sha256 (GNU coreutils).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MANIFEST="${1:-$ROOT/output/manifest.sha256}"

if [[ ! -f "$MANIFEST" ]]; then
  echo "Manifest not found: $MANIFEST" >&2
  echo "Run the engine first to generate evidence." >&2
  exit 1
fi

echo "Verifying hashes from: $MANIFEST"
(
  cd "$(dirname "$MANIFEST")"
  # manifest lines are typically: <hash>  <filename>
  sha256sum -c "$(basename "$MANIFEST")"
)
