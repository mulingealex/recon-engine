"""
PDF Generator.

Generates the final attack surface assessment report.
"""

from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)
from reportlab.lib.units import inch


class PDFGenerator:
    """
    Generates the assessment PDF.
    """

    def __init__(self):
        """
        Initialize the PDF generator.
        """

        self._output_directory = Path(
            "output"
        )

        self._output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    def _add_markdown(
        self,
        story,
        markdown: str,
        styles,
    ):
        """
        Convert simple markdown into
        reportlab paragraphs.

        Parameters
        ----------
        story : list

        markdown : str

        styles : StyleSheet1
        """

        for line in markdown.splitlines():

            line = line.strip()

            if not line:

                story.append(
                    Spacer(
                        1,
                        0.15 * inch,
                    )
                )

                continue

            if line.startswith("# "):

                story.append(
                    Paragraph(
                        f"<b><font size=18>{line[2:]}</font></b>",
                        styles["Heading1"],
                    )
                )

                continue

            if line.startswith("## "):

                story.append(
                    Paragraph(
                        f"<b>{line[3:]}</b>",
                        styles["Heading2"],
                    )
                )

                continue

            if line.startswith("- "):

                story.append(
                    Paragraph(
                        f"• {line[2:]}",
                        styles["BodyText"],
                    )
                )

                continue

            story.append(
                Paragraph(
                    line,
                    styles["BodyText"],
                )
            )

    def generate(
        self,
        executive_summary: str,
        findings: str,
        recommendations: str,
        appendix: str,
    ) -> dict:
        """
        Generate the assessment PDF.

        Parameters
        ----------
        executive_summary : str

        findings : str

        recommendations : str

        appendix : str

        Returns
        -------
        dict
            Metadata describing the
            generated report.
        """

        output_file = (
            self._output_directory /
            "attack-surface-report.pdf"
        )

        document = SimpleDocTemplate(
            str(output_file)
        )

        styles = getSampleStyleSheet()

        story = []

        self._add_markdown(
            story,
            executive_summary,
            styles,
        )

        self._add_markdown(
            story,
            findings,
            styles,
        )

        self._add_markdown(
            story,
            recommendations,
            styles,
        )

        self._add_markdown(
            story,
            appendix,
            styles,
        )

        document.build(
            story
        )

        return {
            "success": True,
            "artifact": "attack-surface-report",
            "filename": output_file.name,
            "path": str(output_file),
            "format": "pdf",
        }


def main():
    """
    Run independently.
    """

    generator = PDFGenerator()

    result = generator.generate(

        "# Executive Summary\nExample summary.",

        "# Findings\nExample findings.",

        "# Recommendations\nExample recommendations.",

        "# Appendix\nExample appendix.",
    )

    print(
        result
    )


if __name__ == "__main__":
    main()