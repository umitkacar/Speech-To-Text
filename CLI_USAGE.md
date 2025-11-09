# 🎯 CLI Usage Guide

Complete guide for using the Speech-To-Text AI command-line interface.

## Installation

```bash
pip install -e .
```

## Quick Start

```bash
# Show version
speech-to-text-ai --version

# Show help
speech-to-text-ai --help

# Listen once
speech-to-text-ai listen

# Continuous recognition
speech-to-text-ai continuous
```

## Commands

### 🎧 `listen` - Listen Once

Recognize speech once from microphone.

```bash
# Basic usage
speech-to-text-ai listen

# Specify language
speech-to-text-ai listen --language tr-TR
speech-to-text-ai listen -l es-ES

# Save to file
speech-to-text-ai listen -o output.txt

# Specify microphone
speech-to-text-ai listen --mic "USB Microphone"

# Set timeout
speech-to-text-ai listen --timeout 20

# Enable verbose logging
speech-to-text-ai listen --verbose
```

**Examples:**

```bash
# English recognition
speech-to-text-ai listen -l en-US

# Turkish recognition with output
speech-to-text-ai listen -l tr-TR -o result.txt

# Spanish with custom timeout
speech-to-text-ai listen -l es-ES -t 30
```

### 🔄 `continuous` - Continuous Recognition

Continuously recognize speech until stopped (Ctrl+C).

```bash
# Basic usage
speech-to-text-ai continuous

# With language
speech-to-text-ai continuous --language en-US

# Limit iterations
speech-to-text-ai continuous --max 10

# Save all results to file
speech-to-text-ai continuous -o transcription.txt

# With custom microphone
speech-to-text-ai continuous --mic "USB Mic" -l tr-TR
```

**Examples:**

```bash
# English continuous mode
speech-to-text-ai continuous -l en-US

# French with output logging
speech-to-text-ai continuous -l fr-FR -o french_transcript.txt

# Limited to 5 recognitions
speech-to-text-ai continuous --max 5
```

### 💬 `interactive` - Interactive Voice Assistant

Recognizes speech and speaks it back using text-to-speech.

```bash
# Basic usage
speech-to-text-ai interactive

# With language
speech-to-text-ai interactive --language en-US

# With custom microphone
speech-to-text-ai interactive --mic "Built-in Microphone"

# Verbose mode
speech-to-text-ai interactive --verbose
```

**Examples:**

```bash
# English interactive mode
speech-to-text-ai interactive -l en-US

# Turkish interactive assistant
speech-to-text-ai interactive -l tr-TR

# German with specific mic
speech-to-text-ai interactive -l de-DE --mic "USB Device"
```

### 🎙️ `devices` - List Microphones

List all available microphone devices.

```bash
# List devices
speech-to-text-ai devices

# Detailed information
speech-to-text-ai devices --detailed
speech-to-text-ai devices -d
```

**Output:**

```
┏━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ ID   ┃ Device Name                   ┃
┡━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ 0    │ Built-in Microphone           │
│ 1    │ USB Audio Device              │
│ 2    │ default                       │
└──────┴───────────────────────────────┘

Total: 3 devices
```

### 🌍 `languages` - List Languages

List all supported languages.

```bash
# List all languages
speech-to-text-ai languages

# Search for specific language
speech-to-text-ai languages --search turkish
speech-to-text-ai languages -s spanish
```

**Output:**

```
┏━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┓
┃ Short Code  ┃ Full Code     ┃ Language             ┃
┡━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━┩
│ en          │ en-US         │ English              │
│ tr          │ tr-TR         │ Turkish (Türkçe)     │
│ es          │ es-ES         │ Spanish (Español)    │
│ fr          │ fr-FR         │ French (Français)    │
│ de          │ de-DE         │ German (Deutsch)     │
└─────────────┴───────────────┴──────────────────────┘
```

### ⚙️ `config` - Configuration Management

Manage application configuration.

```bash
# Show current configuration
speech-to-text-ai config --show

# Save configuration
speech-to-text-ai config --save

# Custom config file
speech-to-text-ai config --show --file ~/my-config.json
```

**Output:**

```
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Setting       ┃ Value             ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ Microphone    │ default           │
│ Sample Rate   │ 48000 Hz          │
│ Language      │ en-US             │
│ Timeout       │ 15s               │
│ TTS Rate      │ 150 wpm           │
└───────────────┴───────────────────┘
```

## Common Options

### Global Options

```bash
--version, -v    # Show version
--help           # Show help
```

### Command Options

```bash
--language, -l   # Language code (e.g., en-US, tr-TR)
--mic, -m        # Microphone device name
--timeout, -t    # Listening timeout (seconds)
--output, -o     # Output file path
--verbose        # Enable verbose logging
--max            # Maximum iterations (continuous mode)
--detailed, -d   # Show detailed information
--search, -s     # Search filter
```

## Language Codes

| Language     | Code  | Short |
| ------------ | ----- | ----- |
| English (US) | en-US | en    |
| Turkish      | tr-TR | tr    |
| Spanish      | es-ES | es    |
| French       | fr-FR | fr    |
| German       | de-DE | de    |
| Italian      | it-IT | it    |
| Portuguese   | pt-PT | pt    |
| Russian      | ru-RU | ru    |
| Japanese     | ja-JP | ja    |
| Korean       | ko-KR | ko    |
| Chinese      | zh-CN | zh    |
| Arabic       | ar-SA | ar    |

## Advanced Usage

### Piping Output

```bash
# Save to file
speech-to-text-ai listen -l en-US > output.txt

# Pipe to other commands
speech-to-text-ai listen -l en-US | grep "keyword"

# Append to file
speech-to-text-ai continuous --max 5 >> transcript.txt
```

### Using with Scripts

```bash
#!/bin/bash

# Continuous transcription script
while true; do
    echo "Listening..."
    result=$(speech-to-text-ai listen -l en-US)
    echo "$(date): $result" >> log.txt

    # Check for stop command
    if [[ $result == *"stop"* ]]; then
        echo "Stopping..."
        break
    fi
done
```

### Environment Variables

```bash
# Set default language
export STT_LANGUAGE="tr-TR"

# Set default microphone
export STT_MICROPHONE="USB Audio"

# Set log level
export STT_LOG_LEVEL="DEBUG"
```

## Keyboard Shortcuts

- `Ctrl+C` - Stop continuous/interactive mode
- `Ctrl+D` - Exit (EOF)
- `Ctrl+Z` - Suspend process

## Troubleshooting

### No audio input

```bash
# Check available devices
speech-to-text-ai devices

# Test with specific device
speech-to-text-ai listen --mic "USB Microphone"
```

### Timeout issues

```bash
# Increase timeout
speech-to-text-ai listen --timeout 30
```

### Language recognition problems

```bash
# Verify language code
speech-to-text-ai languages --search english

# Try different language code
speech-to-text-ai listen -l en-GB  # British English
speech-to-text-ai listen -l en-AU  # Australian English
```

### Verbose debugging

```bash
# Enable verbose logging
speech-to-text-ai listen --verbose

# Check logs
tail -f ~/.config/speech-to-text-ai/logs/app.log
```

## Aliases (Optional)

Add to your `~/.bashrc` or `~/.zshrc`:

```bash
# Short alias
alias stt='speech-to-text-ai'

# Common commands
alias stt-listen='speech-to-text-ai listen'
alias stt-cont='speech-to-text-ai continuous'
alias stt-devices='speech-to-text-ai devices'

# Language-specific
alias stt-en='speech-to-text-ai listen -l en-US'
alias stt-tr='speech-to-text-ai listen -l tr-TR'
alias stt-es='speech-to-text-ai listen -l es-ES'
```

## Integration Examples

### Python Script

```python
import subprocess
import json

# Run recognition
result = subprocess.run(
    ["speech-to-text-ai", "listen", "-l", "en-US"], capture_output=True, text=True
)

print(f"Recognized: {result.stdout}")
```

### Shell Script

```bash
#!/bin/bash

# Meeting transcription
echo "Starting meeting transcription..."
speech-to-text-ai continuous \
    --language en-US \
    --output "meeting_$(date +%Y%m%d_%H%M%S).txt"
```

## Support

- 📖 Documentation: [README.md](README.md)
- 🐛 Issues: [GitHub Issues](https://github.com/umitkacar/Speech-To-Text/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/umitkacar/Speech-To-Text/discussions)
