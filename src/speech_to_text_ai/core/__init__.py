"""Core modules for speech recognition and text-to-speech."""

from speech_to_text_ai.core.recognizer import SpeechRecognizer
from speech_to_text_ai.core.microphone import MicrophoneManager
from speech_to_text_ai.core.speaker import TextToSpeech

__all__ = ["SpeechRecognizer", "MicrophoneManager", "TextToSpeech"]
