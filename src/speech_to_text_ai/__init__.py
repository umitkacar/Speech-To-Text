"""
🎤 Speech-To-Text AI

A modern, powerful speech recognition CLI tool with multi-language support.
"""

__version__ = "1.0.0"
__author__ = "Community Contributors"
__license__ = "MIT"

from speech_to_text_ai.core.recognizer import SpeechRecognizer
from speech_to_text_ai.core.microphone import MicrophoneManager
from speech_to_text_ai.core.speaker import TextToSpeech

__all__ = [
    "SpeechRecognizer",
    "MicrophoneManager",
    "TextToSpeech",
    "__version__",
]
