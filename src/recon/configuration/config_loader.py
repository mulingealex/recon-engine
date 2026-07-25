"""
Configuration loader.

Responsible for loading and merging configuration values.
"""

import argparse
import json
from pathlib import Path
from urllib.parse import urlparse

import yaml


class ConfigLoader:
    """Loads and merges configuration values."""

    def __init__(self):
        """Initialize the configuration loader."""
        pass

    def load(
        self,
        arguments: argparse.Namespace,
    ) -> argparse.Namespace:
        """
        Load configuration values.

        Priority
        --------
        1. Command-line arguments
        2. YAML configuration
        3. Runtime assignment
        """

        #
        # YAML configuration
        #

        if (
            hasattr(arguments, "config")
            and arguments.config is not None
        ):
            self._load_yaml(arguments)

        #
        # Runtime assignment
        #

        if (
            hasattr(arguments, "assignment")
            and arguments.assignment is not None
        ):
            self._load_assignment(arguments)

        #
        # Normalize target regardless of
        # where it came from.
        #

        self._normalize_target(arguments)

        return arguments

    def _load_yaml(
        self,
        arguments: argparse.Namespace,
    ) -> None:
        """
        Load YAML configuration.
        """

        config_path = Path(arguments.config)

        if not config_path.exists():
            raise FileNotFoundError(
                f"Configuration file '{config_path}' was not found."
            )

        try:

            with config_path.open(
                "r",
                encoding="utf-8",
            ) as file:

                configuration = (
                    yaml.safe_load(file)
                    or {}
                )

        except yaml.YAMLError as error:

            raise ValueError(
                f"Invalid YAML configuration: {error}"
            ) from error

        if not isinstance(configuration, dict):
            raise ValueError(
                "Configuration file must contain key-value pairs."
            )

        for key, value in configuration.items():

            if not hasattr(arguments, key):
                continue

            if getattr(arguments, key) is None:

                setattr(
                    arguments,
                    key,
                    value,
                )

    def _load_assignment(
        self,
        arguments: argparse.Namespace,
    ) -> None:
        """
        Load runtime assignment.
        """

        assignment_path = Path(
            arguments.assignment
        )

        if not assignment_path.exists():
            raise FileNotFoundError(
                f"Assignment file '{assignment_path}' was not found."
            )

        with assignment_path.open(
            "r",
            encoding="utf-8",
        ) as file:

            assignment = json.load(file)

        #
        # Runtime metadata.
        #

        arguments.request_budget = assignment.get(
            "request_budget"
        )

        arguments.maximum_rate_per_second = assignment.get(
            "maximum_rate_per_second"
        )

        arguments.runtime_id = assignment.get(
            "runtime_id"
        )

        arguments.profile = assignment.get(
            "profile"
        )

        arguments.marker = assignment.get(
            "marker"
        )

        #
        # Authorized ports.
        #

        authorized_ports = assignment.get(
            "authorized_ports",
            [],
        )

        arguments.authorized_ports = authorized_ports

        if len(authorized_ports) >= 1:
            arguments.web_port = authorized_ports[0]

        if len(authorized_ports) >= 2:
            arguments.signal_port = authorized_ports[1]

        #
        # Use runtime entry URL only when
        # no target was supplied.
        #

        if (
            arguments.target is None
            and assignment.get("entry_url")
        ):
            arguments.target = assignment[
                "entry_url"
            ]

    def _normalize_target(
        self,
        arguments: argparse.Namespace,
    ) -> None:
        """
        Normalize the assessment target.
        """

        if (
            not hasattr(arguments, "target")
            or arguments.target is None
        ):
            return

        target = arguments.target.strip()

        #
        # Add a default scheme if missing.
        #

        if "://" not in target:
            target = f"http://{target}"

        parsed = urlparse(target)

        arguments.entry_url = target

        arguments.scheme = (
            parsed.scheme
        )

        arguments.host = (
            parsed.hostname
        )

        arguments.port = (
            parsed.port
        )

        #
        # Keep the original target unchanged.
        #

        arguments.target = target


if __name__ == "__main__":

    sample = argparse.Namespace(
        target="http://127.0.0.1:18408/",
        scope=None,
        output=None,
        config=None,
        assignment="lab-runtime/assignment.json",
        resume=False,
    )

    loader = ConfigLoader()

    configuration = loader.load(
        sample
    )

    print(configuration)