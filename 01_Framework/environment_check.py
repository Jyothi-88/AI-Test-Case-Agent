
import sys
import platform
from pathlib import Path


def check_environment():
    """Check the basic Python environment for the project."""

    print("AI Test Case Agent - Environment Check")
    print("-" * 40)

    print(f"Python version: {sys.version.split()[0]}")
    print(f"Operating system: {platform.system()}")
    print(f"Project root: {Path(__file__).resolve().parent.parent}")

    print("\nEnvironment check completed.")


if __name__ == "__main__":
    check_environment()
