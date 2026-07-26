"""
Recon Engine package.

Deterministic, scope-aware reconnaissance with evidence integrity
for authorized assessments.

Primary entrypoint
------------------
``python -m recon``

Public subsystems
-----------------
- ``recon.engine`` — top-level workflow coordination
- ``recon.configuration`` — CLI and configuration loading
- ``recon.adapters`` — external tool adapters
- ``recon.discovery`` — discovery pipeline and normalization
- ``recon.evidence`` — assessment evidence writers
- ``recon.reporting`` — attack-surface reporting
"""

from __future__ import annotations

__all__ = [
    "__version__",
]

__version__ = "0.1.0"
