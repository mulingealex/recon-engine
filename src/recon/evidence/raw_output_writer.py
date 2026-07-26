"""
Raw Output Writer.

Persists discovery-stage outputs before normalization.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class RawOutputWriter:
    """
    Writes discovery outputs into ``output/raw-output``.
    """

    def __init__(self) -> None:
        """Create the raw-output directory if needed."""

        self._directory = Path("output") / "raw-output"
        self._directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def write(
        self,
        name: str,
        data: dict[str, Any],
    ) -> Path:
        """
        Persist a single discovery stage payload as JSON.

        Parameters
        ----------
        name:
            Stage name used as the filename stem.
        data:
            Serializable stage result.

        Returns
        -------
        Path
            Destination file path.
        """

        destination = (
            self._directory
            / f"{name}.json"
        )

        destination.write_text(
            json.dumps(
                data,
                indent=2,
                sort_keys=True,
            ),
            encoding="utf-8",
        )

        return destination
