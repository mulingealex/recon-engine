#!/usr/bin/env bash
# Run Recon Engine using an assignment JSON file (authorized labs only).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

ASSIGNMENT="${1:-examples/sample_assignment.json}"
OUTPUT="${2:-output}"

export PYTHONPATH=src

python -m recon \
  --assignment "$ASSIGNMENT" \
  --output "$OUTPUT"
