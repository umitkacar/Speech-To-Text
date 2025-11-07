# 📦 Installation Guide

## Quick Install

### Using pip (Recommended)

```bash
pip install -e .
```

### With Development Tools

```bash
pip install -e ".[dev]"
```

### With All Features

```bash
pip install -e ".[all]"
```

## System Dependencies

### 🐧 Linux (Ubuntu/Debian)

```bash
# Update package list
sudo apt-get update

# Install system audio libraries
sudo apt-get install -y \
    python3-pyaudio \
    portaudio19-dev \
    libportaudio2 \
    libportaudiocpp0 \
    libasound-dev \
    libasound2 \
    alsa-utils \
    alsa-oss

# Install espeak for text-to-speech
sudo apt-get install -y espeak espeak-data libespeak1
```

### 🍎 macOS

```bash
# Install Homebrew (if not already installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install audio dependencies
brew install portaudio

# Install espeak for text-to-speech
brew install espeak
```

### 🪟 Windows

1. Install Python 3.8+ from [python.org](https://www.python.org/downloads/)

2. Install Visual Studio Build Tools:
   - Download from [Visual Studio Downloads](https://visualstudio.microsoft.com/downloads/)
   - Select "Desktop development with C++"

3. Install PyAudio:
   ```powershell
   pip install pipwin
   pipwin install pyaudio
   ```

## Python Package Installation

### From Source (Development)

```bash
# Clone the repository
git clone https://github.com/umitkacar/Speech-To-Text.git
cd Speech-To-Text

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install with development dependencies
pip install -e ".[dev]"

# Setup pre-commit hooks
pre-commit install
```

### Using Hatch (Modern Build System)

```bash
# Install Hatch
pip install hatch

# Create and activate environment
hatch shell

# Run tests
hatch run test

# Run linters
hatch run lint:all
```

## Optional Dependencies

### OpenAI Whisper (Advanced Recognition)

```bash
pip install -e ".[whisper]"
```

### Cloud Services (Google, Azure, Deepgram)

```bash
pip install -e ".[cloud]"
```

### Audio Processing Tools

```bash
pip install -e ".[audio]"
```

## Verify Installation

```bash
# Check CLI is available
speech-to-text-ai --version

# List available microphones
speech-to-text-ai devices

# List supported languages
speech-to-text-ai languages
```

## Troubleshooting

### PyAudio Installation Issues

**Linux:**
```bash
sudo apt-get install python3-dev
pip install --upgrade pip setuptools wheel
pip install pyaudio
```

**macOS:**
```bash
brew install portaudio
pip install pyaudio
```

**Windows:**
```powershell
# Use pipwin for easier installation
pip install pipwin
pipwin install pyaudio
```

### Permission Issues on Linux

```bash
# Add user to audio group
sudo usermod -a -G audio $USER

# Reboot or re-login for changes to take effect
```

### Microphone Access Issues

**Linux:**
```bash
# Test microphone
arecord -l
arecord -d 5 test.wav
aplay test.wav
```

**macOS:**
- Go to System Preferences > Security & Privacy > Microphone
- Enable microphone access for Terminal/iTerm

**Windows:**
- Go to Settings > Privacy > Microphone
- Enable microphone access for Python

## Development Setup

```bash
# Install with all development tools
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install

# Run tests
pytest

# Run linters
ruff check .
black --check .
mypy src/

# Format code
black .
ruff check --fix .
```

## Using Makefile

```bash
# Show all available commands
make help

# Install development dependencies
make dev

# Run tests with coverage
make test-cov

# Format and lint code
make format
make lint

# Run everything
make all
```

## Docker Installation (Optional)

```dockerfile
# Dockerfile example
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    portaudio19-dev \
    python3-pyaudio \
    espeak \
    && rm -rf /var/lib/apt/lists/*

# Install package
COPY . /app
WORKDIR /app
RUN pip install -e .

# Run CLI
ENTRYPOINT ["speech-to-text-ai"]
```

## Next Steps

1. 📖 Read the [README](README.md) for usage examples
2. 💻 Try the CLI: `speech-to-text-ai listen`
3. 🎯 Explore features: `speech-to-text-ai --help`
4. 🤝 Contribute: See [CONTRIBUTING.md](CONTRIBUTING.md)
