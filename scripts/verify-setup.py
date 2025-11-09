#!/usr/bin/env python3
"""
Verify development environment setup.

This script checks that all required tools and configurations are properly installed.
"""

import subprocess
import sys
from pathlib import Path
from typing import Tuple

# Colors for terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"


def check_command(cmd: str, display_name: str = None) -> Tuple[bool, str]:
    """Check if a command is available and get its version."""
    display_name = display_name or cmd
    try:
        result = subprocess.run(
            [cmd, "--version"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
        if result.returncode == 0:
            version = result.stdout.split("\n")[0]
            return True, version
        return False, "Command failed"
    except FileNotFoundError:
        return False, "Not installed"
    except Exception as e:
        return False, str(e)


def check_file(filepath: Path) -> bool:
    """Check if a file exists."""
    return filepath.exists()


def main():
    """Main verification function."""
    print(f"{BLUE}🎤 Speech-To-Text AI - Setup Verification{RESET}")
    print("=" * 60)
    print()

    # Required commands
    commands = [
        ("python3", "Python"),
        ("pip", "pip"),
        ("pytest", "pytest"),
        ("black", "Black"),
        ("ruff", "Ruff"),
        ("mypy", "Mypy"),
        ("pre-commit", "pre-commit"),
        ("hatch", "Hatch"),
    ]

    print(f"{BLUE}📦 Checking Required Tools:{RESET}")
    all_commands_ok = True

    for cmd, name in commands:
        ok, version = check_command(cmd, name)
        if ok:
            print(f"  {GREEN}✓{RESET} {name:15s} {version}")
        else:
            print(f"  {RED}✗{RESET} {name:15s} {version}")
            all_commands_ok = False

    print()

    # Required files
    project_root = Path(__file__).parent.parent
    required_files = [
        "pyproject.toml",
        ".pre-commit-config.yaml",
        "pytest.ini",
        ".coveragerc",
        ".ruff.toml",
        "tox.ini",
        "Makefile",
        "README.md",
        "CONTRIBUTING.md",
        "CODE_OF_CONDUCT.md",
        "INSTALL.md",
        "CLI_USAGE.md",
    ]

    print(f"{BLUE}📁 Checking Configuration Files:{RESET}")
    all_files_ok = True

    for filename in required_files:
        filepath = project_root / filename
        if check_file(filepath):
            size = filepath.stat().st_size
            print(f"  {GREEN}✓{RESET} {filename:30s} ({size:,} bytes)")
        else:
            print(f"  {RED}✗{RESET} {filename:30s} (missing)")
            all_files_ok = False

    print()

    # Check project structure
    required_dirs = [
        "src/speech_to_text_ai",
        "src/speech_to_text_ai/core",
        "src/speech_to_text_ai/config",
        "src/speech_to_text_ai/utils",
        "tests",
        "legacy",
        "scripts",
    ]

    print(f"{BLUE}📂 Checking Project Structure:{RESET}")
    all_dirs_ok = True

    for dirname in required_dirs:
        dirpath = project_root / dirname
        if dirpath.is_dir():
            file_count = len(list(dirpath.glob("*.py")))
            print(f"  {GREEN}✓{RESET} {dirname:35s} ({file_count} .py files)")
        else:
            print(f"  {RED}✗{RESET} {dirname:35s} (missing)")
            all_dirs_ok = False

    print()

    # Check Python imports
    print(f"{BLUE}🐍 Checking Python Imports:{RESET}")
    imports_to_check = [
        ("speech_recognition", "SpeechRecognition"),
        ("pyttsx3", "pyttsx3"),
        ("typer", "Typer"),
        ("rich", "Rich"),
    ]

    all_imports_ok = True
    for module, name in imports_to_check:
        try:
            __import__(module)
            print(f"  {GREEN}✓{RESET} {name:20s} importable")
        except ImportError:
            print(f"  {RED}✗{RESET} {name:20s} not importable")
            all_imports_ok = False

    print()

    # Check our package
    print(f"{BLUE}📦 Checking Package Installation:{RESET}")
    try:
        import speech_to_text_ai

        version = speech_to_text_ai.__version__
        print(f"  {GREEN}✓{RESET} speech-to-text-ai v{version} is installed")
        package_ok = True
    except ImportError:
        print(f"  {RED}✗{RESET} speech-to-text-ai is not installed")
        print(f"  {YELLOW}💡{RESET} Run: pip install -e .")
        package_ok = False

    print()

    # Summary
    print("=" * 60)
    all_ok = all_commands_ok and all_files_ok and all_dirs_ok and all_imports_ok and package_ok

    if all_ok:
        print(f"{GREEN}✓ All checks passed! Development environment is ready.{RESET}")
        return 0
    else:
        print(f"{RED}✗ Some checks failed. Please review the output above.{RESET}")
        print()
        print(f"{YELLOW}💡 Quick fixes:{RESET}")
        if not all_commands_ok:
            print("   - Install dev dependencies: make dev")
        if not package_ok:
            print("   - Install package: pip install -e .")
        if not all_imports_ok:
            print("   - Install requirements: pip install -r requirements.txt")
        return 1


if __name__ == "__main__":
    sys.exit(main())
