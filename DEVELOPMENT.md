# 🛠️ Development Guide

Complete guide for developers contributing to Speech-To-Text AI.

## 🚀 Quick Start

### 1. Clone Repository

```bash
git clone https://github.com/umitkacar/Speech-To-Text.git
cd Speech-To-Text
```

### 2. Setup Development Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Automated setup
bash scripts/setup-dev.sh

# Or manual setup
make dev
make setup-hooks
```

### 3. Verify Setup

```bash
# Verify everything is installed
make verify
# or
python scripts/verify-setup.py
```

## 📦 Development Tools

### Hatch - Build System

```bash
# Create environment
hatch env create

# Shell into environment
hatch shell

# Run tests
hatch run test

# Run linters
hatch run lint:all

# Build package
hatch build
```

### Tox - Multi-Environment Testing

```bash
# Test all Python versions
tox

# Test specific environment
tox -e py310
tox -e lint
tox -e coverage

# Parallel execution
tox -p auto
```

### Pre-commit - Code Quality

```bash
# Install hooks
pre-commit install

# Run manually
pre-commit run --all-files

# Run specific hook
pre-commit run black
pre-commit run ruff

# Update hooks
pre-commit autoupdate
```

## 🧪 Testing

### Running Tests

```bash
# All tests
make test

# With coverage
make test-cov

# Watch mode (requires pytest-watch)
make test-watch

# Specific test file
pytest tests/test_recognizer.py

# Specific test
pytest tests/test_recognizer.py::TestSpeechRecognizer::test_initialization

# With markers
pytest -m unit
pytest -m "not slow"
```

### Writing Tests

```python
import pytest
from speech_to_text_ai import SpeechRecognizer


class TestSpeechRecognizer:
    """Test SpeechRecognizer class."""

    def test_initialization(self):
        """Test recognizer initialization."""
        recognizer = SpeechRecognizer(language="en-US")
        assert recognizer.language == "en-US"

    @pytest.mark.slow
    def test_recognition(self):
        """Test actual recognition (slow)."""
        # Test implementation
        pass
```

### Test Markers

- `@pytest.mark.unit` - Unit tests
- `@pytest.mark.integration` - Integration tests
- `@pytest.mark.slow` - Slow tests (skip in CI)
- `@pytest.mark.smoke` - Smoke tests

## 🎨 Code Style

### Formatting with Black

```bash
# Format code
make format

# Check formatting
black --check src/ tests/

# Format specific file
black src/speech_to_text_ai/cli.py
```

### Linting with Ruff

```bash
# Lint code
make lint

# Auto-fix issues
ruff check --fix src/ tests/

# Check specific rules
ruff check --select E,F src/
```

### Type Checking with Mypy

```bash
# Check types
mypy src/

# Check with strict mode
mypy --strict src/

# Generate type stubs
stubgen -p speech_to_text_ai -o stubs/
```

## 🔒 Security

### Bandit - Security Linting

```bash
# Run security checks
make security

# Generate report
bandit -r src/ -f json -o bandit-report.json

# Check specific issue
bandit -r src/ -t B201,B301
```

### Security Best Practices

- ✅ No hardcoded secrets
- ✅ Input validation
- ✅ No SQL injection
- ✅ Secure random (use secrets module)
- ✅ No eval/exec

## 📊 Coverage

### Generating Coverage Reports

```bash
# HTML report
make test-cov
open htmlcov/index.html

# Terminal report
pytest --cov=src/speech_to_text_ai --cov-report=term-missing

# XML report (for CI)
pytest --cov=src/speech_to_text_ai --cov-report=xml
```

### Coverage Requirements

| Component | Minimum |
| --------- | ------- |
| Overall   | 75%     |
| Core      | 80%     |
| Utils     | 70%     |
| CLI       | 60%     |

## 🏗️ Project Structure

```
src/speech_to_text_ai/
├── __init__.py          # Package initialization
├── __main__.py          # Entry point
├── cli.py               # CLI interface (Typer)
├── core/                # Core functionality
│   ├── recognizer.py    # Speech recognition
│   ├── microphone.py    # Microphone management
│   └── speaker.py       # Text-to-speech
├── config/              # Configuration
│   └── settings.py      # Settings management
└── utils/               # Utilities
    └── logger.py        # Logging
```

## 🔄 Git Workflow

### Branch Naming

- `feature/` - New features
- `fix/` - Bug fixes
- `docs/` - Documentation
- `refactor/` - Code refactoring
- `test/` - Test additions

### Commit Messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add continuous recognition mode
fix: handle timeout errors gracefully
docs: update CLI usage guide
refactor: simplify microphone selection
test: add tests for TTS module
```

### Pre-commit Checks

Every commit runs:

- ✅ Black formatting
- ✅ Ruff linting
- ✅ isort import sorting
- ✅ mypy type checking
- ✅ Bandit security
- ✅ File checks

## 📝 Documentation

### Docstring Style (Google)

```python
def recognize_once(self, show_prompt: bool = True) -> RecognitionResult:
    """
    Recognize speech once from microphone.

    Args:
        show_prompt: Whether to show listening prompt

    Returns:
        RecognitionResult with recognized text or error

    Raises:
        TimeoutError: If no speech detected within timeout

    Example:
        >>> recognizer = SpeechRecognizer()
        >>> result = recognizer.recognize_once()
        >>> print(result.text)
        'hello world'
    """
    pass
```

### Type Hints

Always use type hints:

```python
from typing import Optional, List, Dict, Any


def process_audio(
    audio_data: bytes, language: str = "en-US", timeout: Optional[int] = None
) -> Dict[str, Any]:
    """Process audio data."""
    pass
```

## 🚀 Release Process

### 1. Version Bump

```bash
# Update version in:
# - pyproject.toml
# - src/speech_to_text_ai/__init__.py

# Update CHANGELOG.md
```

### 2. Test Everything

```bash
# Run full test suite
tox

# Run quality checks
make quality

# Verify setup
make verify
```

### 3. Build & Test Package

```bash
# Build package
hatch build

# Test installation
pip install dist/*.whl

# Test CLI
speech-to-text-ai --version
speech-to-text-ai --help
```

### 4. Tag & Release

```bash
# Create tag
git tag -a v1.0.0 -m "Release v1.0.0"

# Push tag
git push origin v1.0.0

# Publish to PyPI (if configured)
hatch publish
```

## 🐛 Debugging

### Enable Debug Logging

```bash
# CLI with verbose
speech-to-text-ai listen --verbose

# Python with debug
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Common Issues

#### Import Errors

```bash
# Reinstall in editable mode
pip install -e .
```

#### PyAudio Issues

```bash
# Linux
sudo apt-get install portaudio19-dev python3-pyaudio

# macOS
brew install portaudio

# Windows
pip install pipwin
pipwin install pyaudio
```

#### Pre-commit Failures

```bash
# Update hooks
pre-commit autoupdate

# Clear cache
pre-commit clean

# Reinstall
pre-commit uninstall
pre-commit install
```

## 📊 Makefile Commands

```bash
# Setup
make dev              # Install dev dependencies
make setup-dev        # Run setup script
make verify           # Verify setup

# Testing
make test             # Run tests
make test-cov         # Tests with coverage
make tox              # Multi-version tests

# Code Quality
make format           # Format code
make lint             # Lint code
make security         # Security checks
make quality          # All quality checks

# CI/CD
make ci               # Run CI pipeline locally

# Utilities
make clean            # Clean build artifacts
make info             # Show project info
make help             # Show all commands
```

## 🎯 Best Practices

### Code Quality

1. **Write tests first** (TDD)
1. **Keep functions small** (\< 50 lines)
1. **Use type hints** everywhere
1. **Document public APIs**
1. **Handle errors gracefully**

### Performance

1. **Profile before optimizing**
1. **Use appropriate data structures**
1. **Avoid premature optimization**
1. **Cache expensive operations**

### Security

1. **Never commit secrets**
1. **Validate all inputs**
1. **Use secrets module for random**
1. **Keep dependencies updated**

## 📚 Resources

### Official Docs

- [Python Documentation](https://docs.python.org/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Hatch Documentation](https://hatch.pypa.io/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)

### Style Guides

- [PEP 8](https://pep8.org/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Type Hints PEP 484](https://www.python.org/dev/peps/pep-0484/)

### Tools

- [Black](https://black.readthedocs.io/)
- [Ruff](https://docs.astral.sh/ruff/)
- [Mypy](https://mypy.readthedocs.io/)
- [Pre-commit](https://pre-commit.com/)

## 🤝 Getting Help

- 📖 Check [README.md](README.md)
- 🐛 Search [Issues](https://github.com/umitkacar/Speech-To-Text/issues)
- 💬 Start a [Discussion](https://github.com/umitkacar/Speech-To-Text/discussions)
- 📧 Contact maintainers

______________________________________________________________________

**Happy Coding! 🚀**
