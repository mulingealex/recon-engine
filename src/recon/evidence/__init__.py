"""
Evidence package.

Writers that materialize assessment artifacts (JSON, CSV, Markdown,
text, and SHA-256 manifests) from normalized discovery results.
"""

from .orchestrator import EvidenceOrchestrator

from .normalized_writer import NormalizedWriter
from .scope_register_writer import ScopeRegisterWriter
from .request_ledger_writer import RequestLedgerWriter
from .evidence_index_writer import EvidenceIndexWriter
from .assessment_manifest_writer import (
    AssessmentManifestWriter,
)
from .continuity_writer import ContinuityWriter
from .integrity_writer import IntegrityWriter
from .manifest_writer import ManifestWriter
from .raw_output_writer import RawOutputWriter

__all__ = [
    "EvidenceOrchestrator",
    "NormalizedWriter",
    "ScopeRegisterWriter",
    "RequestLedgerWriter",
    "EvidenceIndexWriter",
    "AssessmentManifestWriter",
    "ContinuityWriter",
    "IntegrityWriter",
    "ManifestWriter",
    "RawOutputWriter",
]