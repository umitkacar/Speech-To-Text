from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="speech-to-text-ai",
    version="1.0.0",
    author="Community Contributors",
    author_email="",
    description="🎤 Real-time Speech Recognition powered by Google AI with multi-language support",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/umitkacar/Speech-To-Text",
    project_urls={
        "Bug Tracker": "https://github.com/umitkacar/Speech-To-Text/issues",
        "Documentation": "https://github.com/umitkacar/Speech-To-Text#readme",
        "Source Code": "https://github.com/umitkacar/Speech-To-Text",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "SpeechRecognition>=3.10.1",
        "PyAudio>=0.2.14",
        "pyttsx3>=2.90",
    ],
    extras_require={
        "dev": [
            "pytest>=8.0.0",
            "black>=24.1.0",
            "flake8>=7.0.0",
            "pytest-cov>=4.1.0",
        ],
        "whisper": [
            "openai-whisper",
            "faster-whisper",
        ],
        "cloud": [
            "google-cloud-speech>=2.24.0",
            "azure-cognitiveservices-speech>=1.35.0",
            "deepgram-sdk>=3.2.0",
        ],
    },
    keywords=[
        "speech-recognition",
        "speech-to-text",
        "voice-recognition",
        "audio-processing",
        "ai",
        "machine-learning",
        "natural-language-processing",
        "google-speech-api",
        "whisper",
        "asr",
    ],
)
