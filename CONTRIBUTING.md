# 🤝 Contributing to Speech-To-Text AI

First off, thank you for considering contributing to Speech-To-Text AI! It's people like you that make this project such a great tool.

## 🌟 Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## 🎯 How Can I Contribute?

### 🐛 Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps to reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why**
* **Include screenshots if possible**

### 💡 Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior and explain the behavior you expected to see**
* **Explain why this enhancement would be useful**

### 🔧 Pull Requests

* Fill in the required template
* Do not include issue numbers in the PR title
* Follow the Python style guide (PEP 8)
* Include thoughtfully-worded, well-structured tests
* Document new code
* End all files with a newline

## 💻 Development Process

### 1. Fork & Clone

```bash
# Fork the repo on GitHub, then:
git clone https://github.com/YOUR_USERNAME/Speech-To-Text.git
cd Speech-To-Text
```

### 2. Create a Branch

```bash
git checkout -b feature/amazing-feature
# or
git checkout -b fix/bug-fix
```

### 3. Set Up Development Environment

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install pytest black flake8
```

### 4. Make Your Changes

* Write clean, readable code
* Follow PEP 8 style guidelines
* Add comments for complex logic
* Update documentation if needed

### 5. Test Your Changes

```bash
# Run tests
pytest

# Check code style
black .
flake8 .
```

### 6. Commit Your Changes

```bash
git add .
git commit -m "Add: Brief description of changes"
```

**Commit Message Guidelines:**
* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests after the first line

**Commit Prefixes:**
* `Add:` - New feature
* `Fix:` - Bug fix
* `Update:` - Update existing feature
* `Refactor:` - Code refactoring
* `Docs:` - Documentation changes
* `Test:` - Adding or updating tests
* `Style:` - Code style changes

### 7. Push to GitHub

```bash
git push origin feature/amazing-feature
```

### 8. Open a Pull Request

* Go to your fork on GitHub
* Click "Pull Request"
* Fill in the PR template
* Link related issues

## 📝 Style Guide

### Python Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with some modifications:

```python
# Good
def recognize_speech(audio_source, language='en-US'):
    """
    Recognize speech from audio source.

    Args:
        audio_source: Audio input source
        language: Language code (default: 'en-US')

    Returns:
        str: Recognized text
    """
    recognizer = sr.Recognizer()
    try:
        text = recognizer.recognize_google(audio_source, language=language)
        return text
    except sr.UnknownValueError:
        return None
```

### Documentation Style

* Use docstrings for all public modules, functions, classes, and methods
* Follow Google style docstrings
* Include examples in docstrings when helpful

## 🧪 Testing Guidelines

* Write tests for all new features
* Ensure all tests pass before submitting PR
* Aim for high code coverage
* Test edge cases

```python
def test_speech_recognition():
    """Test basic speech recognition functionality."""
    # Test implementation
    assert True
```

## 📦 Project Structure

```
Speech-To-Text/
├── .github/              # GitHub specific files
│   ├── ISSUE_TEMPLATE/
│   └── workflows/
├── docs/                 # Documentation
├── tests/                # Test files
├── examples/             # Example scripts
├── google_api_1.py       # Basic implementation
├── google_api_2.py       # Advanced implementation
├── google_api_3_return.py # Interactive implementation
├── requirements.txt      # Dependencies
├── README.md            # Main documentation
├── CONTRIBUTING.md      # This file
└── LICENSE              # License file
```

## 🎨 Adding New Features

When adding new features:

1. **Discuss First** - Open an issue to discuss major changes
2. **Keep It Simple** - Follow KISS principle
3. **Maintain Compatibility** - Don't break existing functionality
4. **Document Everything** - Update README and code comments
5. **Add Examples** - Include usage examples
6. **Test Thoroughly** - Write comprehensive tests

## 🔍 Code Review Process

1. At least one maintainer must review and approve
2. All tests must pass
3. Code must follow style guidelines
4. Documentation must be updated
5. No merge conflicts

## 🌈 Recognition

Contributors will be recognized in:
* README.md (Contributors section)
* Release notes
* GitHub contributors page

## 📞 Questions?

Feel free to:
* Open an issue with the `question` label
* Start a discussion on GitHub Discussions
* Contact the maintainers

## 🎉 Thank You!

Your contributions to open source, large or small, make projects like this possible. Thank you for taking the time to contribute!

---

**Happy Coding! 🚀**
