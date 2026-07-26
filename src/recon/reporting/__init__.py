"""
Reporting package.

Attack-surface assessment sections and PDF generation.
"""

from .orchestrator import ReportingOrchestrator

from .executive_summary_writer import (
    ExecutiveSummaryWriter,
)

from .findings_writer import (
    FindingsWriter,
)

from .recommendations_writer import (
    RecommendationsWriter,
)

from .appendix_writer import (
    AppendixWriter,
)

from .pdf_generator import (
    PDFGenerator,
)

__all__ = [
    "ReportingOrchestrator",
    "ExecutiveSummaryWriter",
    "FindingsWriter",
    "RecommendationsWriter",
    "AppendixWriter",
    "PDFGenerator",
]