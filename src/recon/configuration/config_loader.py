"""
Configuration loader.

Responsible for loading and merging configuration values.
"""

import argparse
from pathlib import Path

import yaml


class ConfigLoader:
    """Loads and merges configuration values."""

    def __init__(self):
        """Initialize the configuration loader."""
        pass

    def load(self, arguments: argparse.Namespace) -> argparse.Namespace:
        """
        Load configuration values and merge them into the parsed
        command-line arguments.

        Parameters
        ----------
        arguments : argparse.Namespace
            Parsed command-line arguments.

        Returns
        -------
        argparse.Namespace
            Updated configuration.
        """

        # No configuration file supplied.
        if arguments.config is None:
            return arguments

        config_path = Path(arguments.config)

        # Verify the configuration file exists.
        if not config_path.exists():
            raise FileNotFoundError(
                f"Configuration file '{config_path}' was not found."
            )

        # Load the YAML configuration.
        try:
            with config_path.open("r", encoding="utf-8") as file:
                configuration = yaml.safe_load(file) or {}

        except yaml.YAMLError as error:
            raise ValueError(
                f"Invalid YAML configuration: {error}"
            ) from error

        # Ensure the root object is a dictionary.
        if not isinstance(configuration, dict):
            raise ValueError(
                "Configuration file must contain key-value pairs."
            )

        # Merge configuration values.
        for key, value in configuration.items():

            # Ignore unknown configuration keys.
            if not hasattr(arguments, key):
                continue

            # Command-line arguments always take precedence.
            if getattr(arguments, key) is None:
                setattr(arguments, key, value)

        return arguments


if __name__ == "__main__":

    sample = argparse.Namespace(
        target=None,
        scope=None,
        output=None,
        config="config.yaml",
        resume=False,
    )

    loader = ConfigLoader()

    configuration = loader.load(sample)

    print(configuration)