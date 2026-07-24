"""
Scope validator.

Responsible for validating reconnaissance scope before execution.
"""

import argparse
from pathlib import Path


class ScopeValidator:
    """Validates the reconnaissance scope."""

    def __init__(self):
        """Initialize the scope validator."""
        pass

    def validate(self, arguments: argparse.Namespace) -> argparse.Namespace:
        """
        Validate the supplied arguments.

        Parameters
        ----------
        arguments : argparse.Namespace
            Parsed and merged configuration.

        Returns
        -------
        argparse.Namespace
            Validated arguments.
        """

        # Target is required unless resuming.
        if not arguments.resume and not arguments.target:
            raise ValueError(
                "A target must be provided unless resuming."
            )

        # Reject empty targets.
        if arguments.target is not None:

            if not arguments.target.strip():
                raise ValueError(
                    "Target cannot be empty."
                )

        # Scope file must exist.
        if arguments.scope is not None:

            scope_path = Path(arguments.scope)

            if not scope_path.is_file():
                raise FileNotFoundError(
                    f"Scope file '{scope_path}' was not found."
                )

        return arguments


if __name__ == "__main__":

    sample = argparse.Namespace(
        target=None,
        scope="scope.txt",
        output="reports/",
        config=None,
        resume=True,
    )

    validator = ScopeValidator()

    validated = validator.validate(sample)

    print(validated)