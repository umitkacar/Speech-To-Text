<div align="center">

# 🎤 Speech-To-Text AI

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=32&duration=2800&pause=2000&color=2E9EF7&center=true&vCenter=true&width=940&lines=Real-Time+Speech+Recognition;Powered+by+Google+AI;Multi-Language+Support;Voice+Interactive+System" alt="Typing SVG" />

[![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Google Cloud](https://img.shields.io/badge/Google%20Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)](https://cloud.google.com/speech-to-text)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Stars](https://img.shields.io/github/stars/umitkacar/Speech-To-Text?style=for-the-badge&logo=github)](https://github.com/umitkacar/Speech-To-Text/stargazers)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge)](http://makeapullrequest.com)

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-examples">Examples</a> •
  <a href="#-trending-resources">Resources</a> •
  <a href="#-roadmap">Roadmap</a> •
  <a href="#-contributing">Contributing</a>
</p>

</div>

---

## 🚀 Features

<table>
<tr>
<td>

### 🎯 Core Capabilities
- 🗣️ **Real-time Speech Recognition** - Instant voice-to-text conversion
- 🌍 **Multi-Language Support** - Support for 100+ languages
- 🎙️ **Microphone Integration** - Easy device selection and management
- 🔄 **Bidirectional Communication** - Speech-to-Text & Text-to-Speech
- ⚡ **Low Latency** - Optimized for real-time applications
- 🎨 **Multiple APIs** - Google, Azure, AWS support ready

</td>
<td>

### 💡 Advanced Features
- 🧠 **AI-Powered** - Google Cloud AI integration
- 🔊 **Noise Cancellation** - Ambient noise adjustment
- 📊 **Custom Sample Rates** - Configurable audio parameters
- 🔌 **Offline Mode** - CMU Sphinx support
- 🎛️ **Audio Controls** - ALSA mixer integration
- 📝 **Multiple Outputs** - Text, JSON, structured data

</td>
</tr>
</table>

---

## 📦 Quick Start

### Prerequisites

```bash
# Python 3.7 or higher
python3 --version
```

### Installation

#### 🐧 Linux (Ubuntu/Debian)

```bash
# Clone the repository
git clone https://github.com/umitkacar/Speech-To-Text.git
cd Speech-To-Text

# Install Python dependencies
sudo -H pip3 install SpeechRecognition PyAudio pyttsx3

# Install system dependencies
sudo apt-get update
sudo apt-get install -y \
    python3-pyaudio \
    portaudio19-dev \
    libportaudio2 \
    libportaudiocpp0 \
    libasound-dev \
    libasound2 \
    alsa-utils \
    alsa-oss
```

#### 🍎 macOS

```bash
# Install Homebrew dependencies
brew install portaudio

# Install Python packages
pip3 install SpeechRecognition PyAudio pyttsx3
```

#### 🪟 Windows

```bash
# Install Python packages
pip install SpeechRecognition PyAudio pyttsx3
```

> **Note**: On Windows, you may need to install [Visual Studio Build Tools](https://visualstudio.microsoft.com/downloads/) for PyAudio.

---

## 💻 Usage

### Example 1: Basic Speech Recognition

```python
import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Use microphone as source
with sr.Microphone() as source:
    print("🎤 Say something!")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='en-US')
        print(f"✅ You said: {text}")
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError as e:
        print(f"⚠️ Error: {e}")
```

### Example 2: Advanced Configuration

```python
# Custom configuration
mic_name = 'default'
sample_rate = 48000
chunk_size = 2048

r = sr.Recognizer()

with sr.Microphone(
    device_index=device_id,
    sample_rate=sample_rate,
    chunk_size=chunk_size
) as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, timeout=15)
    text = r.recognize_google(audio, language='TR')
```

### Example 3: Interactive Voice Assistant

```python
import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio, language='en-US')
            print(f"📝 You said: {text}")
            speak(text)
        except:
            print("❌ Error occurred")
```

---

## 📂 Examples

| File | Description | Use Case |
|------|-------------|----------|
| `google_api_1.py` | Basic speech recognition | Simple voice-to-text conversion |
| `google_api_2.py` | Advanced configuration | Production applications with custom settings |
| `google_api_3_return.py` | Interactive voice system | Voice assistants, chatbots |

---

## 🎯 Trending Resources (2024-2025)

### 🔥 Top Speech-to-Text Projects & Libraries

#### Modern AI Models (2024-2025)

| Project | Description | Stars | Tech |
|---------|-------------|-------|------|
| [**Whisper**](https://github.com/openai/whisper) | OpenAI's robust speech recognition (SOTA 2024) | ![Stars](https://img.shields.io/github/stars/openai/whisper?style=social) | PyTorch, Transformers |
| [**Faster Whisper**](https://github.com/guillaumekln/faster-whisper) | Optimized Whisper implementation (4x faster) | ![Stars](https://img.shields.io/github/stars/guillaumekln/faster-whisper?style=social) | CTranslate2 |
| [**Whisper.cpp**](https://github.com/ggerganov/whisper.cpp) | C++ port of Whisper (edge devices) | ![Stars](https://img.shields.io/github/stars/ggerganov/whisper.cpp?style=social) | C++, WASM |
| [**Vosk**](https://github.com/alphacep/vosk-api) | Offline speech recognition (100+ languages) | ![Stars](https://img.shields.io/github/stars/alphacep/vosk-api?style=social) | Kaldi |
| [**SpeechBrain**](https://github.com/speechbrain/speechbrain) | All-in-one speech toolkit | ![Stars](https://img.shields.io/github/stars/speechbrain/speechbrain?style=social) | PyTorch |
| [**Wav2Vec 2.0**](https://github.com/facebookresearch/fairseq) | Meta's self-supervised speech model | ![Stars](https://img.shields.io/github/stars/facebookresearch/fairseq?style=social) | PyTorch |
| [**NeMo ASR**](https://github.com/NVIDIA/NeMo) | NVIDIA's conversational AI toolkit | ![Stars](https://img.shields.io/github/stars/NVIDIA/NeMo?style=social) | PyTorch |

#### Real-Time & Production Ready

| Project | Description | Use Case |
|---------|-------------|----------|
| [**Deepgram SDK**](https://github.com/deepgram/deepgram-python-sdk) | Production-grade ASR API | Enterprise applications |
| [**AssemblyAI**](https://github.com/AssemblyAI/assemblyai-python-sdk) | Modern speech-to-text API | Real-time transcription |
| [**Azure Speech SDK**](https://github.com/Azure-Samples/cognitive-services-speech-sdk) | Microsoft's Speech Services | Cloud integration |
| [**Amazon Transcribe**](https://aws.amazon.com/transcribe/) | AWS speech recognition | Scalable solutions |

#### Specialized & Emerging (2024-2025)

| Project | Innovation | GitHub |
|---------|------------|--------|
| [**Distil-Whisper**](https://github.com/huggingface/distil-whisper) | 6x faster Whisper variant | ⭐ Trending |
| [**Seamless M4T**](https://github.com/facebookresearch/seamless_communication) | Multilingual speech translation | Meta AI |
| [**MMS (Massively Multilingual Speech)**](https://github.com/facebookresearch/fairseq/tree/main/examples/mms) | 1000+ languages support | Meta Research |
| [**Canary**](https://github.com/NVIDIA/NeMo) | NVIDIA's multilingual ASR | SOTA 2024 |

### 🎓 Learning Resources

- 📚 [**Speech Recognition Course**](https://www.deeplearning.ai/courses/natural-language-processing-specialization/) - DeepLearning.AI
- 🎥 [**Whisper Tutorial Series**](https://www.youtube.com/results?search_query=openai+whisper+tutorial+2024) - Latest tutorials
- 📖 [**ASR Papers**](https://paperswithcode.com/task/speech-recognition) - State-of-the-art research
- 🛠️ [**Hugging Face Audio**](https://huggingface.co/tasks/automatic-speech-recognition) - Pre-trained models

### 🔧 Development Tools (2024-2025)

- 🎛️ [**Audio Processing**](https://github.com/jiaaro/pydub) - Modern audio manipulation
- 🎚️ [**Noise Reduction**](https://github.com/timsainb/noisereduce) - AI-powered noise cancellation
- 📊 [**Speech Analytics**](https://github.com/tyiannak/pyAudioAnalysis) - Audio feature extraction
- 🎵 [**Librosa**](https://github.com/librosa/librosa) - Audio analysis library

### ☁️ Cloud Services Comparison (2024-2025)

| Service | Accuracy | Speed | Languages | Free Tier | Best For |
|---------|----------|-------|-----------|-----------|----------|
| **Google Cloud Speech** | ⭐⭐⭐⭐⭐ | Fast | 125+ | 60 min/month | General purpose |
| **Deepgram** | ⭐⭐⭐⭐⭐ | Very Fast | 30+ | $200 credit | Real-time apps |
| **AssemblyAI** | ⭐⭐⭐⭐⭐ | Fast | 15+ | 5 hours | Transcription |
| **Azure Speech** | ⭐⭐⭐⭐ | Medium | 100+ | 5 hours | Enterprise |
| **Amazon Transcribe** | ⭐⭐⭐⭐ | Fast | 35+ | 60 min/month | AWS ecosystem |
| **Whisper (Self-hosted)** | ⭐⭐⭐⭐⭐ | Medium | 99 | Free | Privacy-first |

---

## 🛠️ Technology Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

</div>

---

## 🗺️ Roadmap

### 2024 Q4 - 2025 Q1

- [x] ✅ Basic speech recognition
- [x] ✅ Multi-language support
- [x] ✅ Microphone integration
- [ ] 🚧 **Whisper integration** (OpenAI SOTA model)
- [ ] 🚧 **Real-time streaming** (WebSocket support)
- [ ] 🚧 **Docker containerization**
- [ ] 📋 **GPU acceleration** (CUDA support)
- [ ] 📋 **Web interface** (React dashboard)
- [ ] 📋 **API endpoints** (FastAPI/Flask)
- [ ] 📋 **Multilingual models** (Seamless M4T)
- [ ] 📋 **Speaker diarization** (Who spoke when)
- [ ] 📋 **Emotion detection** (Sentiment analysis)

---

## 🔧 Audio Configuration

### Check Available Microphones

```bash
# List all audio devices
python -c "import speech_recognition as sr; print(sr.Microphone.list_microphone_names())"
```

### ALSA Controls (Linux)

```bash
# Open mixer
alsamixer

# Command line mixer
amixer

# Test recording
arecord -l
```

---

## 🤝 Contributing

Contributions are what make the open source community amazing! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=umitkacar/Speech-To-Text&type=Date)](https://star-history.com/#umitkacar/Speech-To-Text&Date)

---

## 📞 Contact & Support

<div align="center">

[![GitHub Issues](https://img.shields.io/badge/Issues-Ask_a_Question-blue?style=for-the-badge&logo=github)](https://github.com/umitkacar/Speech-To-Text/issues)
[![GitHub Discussions](https://img.shields.io/badge/Discussions-Join_Chat-green?style=for-the-badge&logo=github)](https://github.com/umitkacar/Speech-To-Text/discussions)

</div>

---

## 🙏 Acknowledgments

- [OpenAI Whisper](https://github.com/openai/whisper) - Inspiration for modern ASR
- [SpeechRecognition](https://github.com/Uberi/speech_recognition) - Core library
- [Google Cloud Speech](https://cloud.google.com/speech-to-text) - API provider
- [PyTTSx3](https://github.com/nateshmbhat/pyttsx3) - Text-to-speech engine

---

<div align="center">

### ⭐ If this project helped you, please consider giving it a star!

Made with ❤️ by the community

</div>
