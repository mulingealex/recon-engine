"""
Recon package entry point.
"""

from recon.engine import ReconEngine

from argparse import ArgumentParser


def main() -> None:
    parser = ArgumentParser(
        description="Recon Engine"
    )

    parser.add_argument(
        "target",
        help="Target hostname or domain",
    )

    arguments = parser.parse_args()

    engine = ReconEngine()

    results = engine.execute(arguments)

    print("\nAssessment completed successfully.\n")
    print(f"Target: {results['target']}\n")

    print("Artifacts:")

    for artifact, path in results["artifacts"].items():
        print(f"  ✓ {artifact}: {path}")


if __name__ == "__main__":
    main()