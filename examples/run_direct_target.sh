#!/usr/bin/env bash
# Run Recon Engine against a direct target (authorized labs only).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

TARGET="${1:-127.0.0.1}"
OUTPUT="${2:-output}"

export PYTHONPATH=src

python -m recon "$TARGET" --output "$OUTPUT"
