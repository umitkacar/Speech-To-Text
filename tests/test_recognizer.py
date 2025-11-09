"""Tests for speech recognizer."""

from speech_to_text_ai.core.microphone import MicrophoneManager
from speech_to_text_ai.core.recognizer import RecognitionResult, SpeechRecognizer


class TestRecognitionResult:
    """Test RecognitionResult class."""

    def test_success_result(self):
        """Test successful recognition result."""
        result = RecognitionResult(text="hello world", success=True)

        assert result.text == "hello world"
        assert result.success is True
        assert result.error is None
        assert str(result) == "✓ hello world"

    def test_error_result(self):
        """Test error recognition result."""
        result = RecognitionResult(success=False, error="API error")

        assert result.text is None
        assert result.success is False
        assert result.error == "API error"
        assert str(result) == "✗ API error"

    def test_to_dict(self):
        """Test conversion to dictionary."""
        result = RecognitionResult(text="test", success=True, confidence=0.95)
        result_dict = result.to_dict()

        assert result_dict["text"] == "test"
        assert result_dict["success"] is True
        assert result_dict["confidence"] == 0.95
        assert result_dict["error"] is None


class TestSpeechRecognizer:
    """Test SpeechRecognizer class."""

    def test_initialization(self):
        """Test recognizer initialization."""
        recognizer = SpeechRecognizer(language="tr-TR", timeout=10)

        assert recognizer.language == "tr-TR"
        assert recognizer.timeout == 10
        assert recognizer.recognizer is not None
        assert recognizer.mic_manager is not None

    def test_default_initialization(self):
        """Test recognizer with defaults."""
        recognizer = SpeechRecognizer()

        assert recognizer.language == "en-US"
        assert recognizer.timeout == 15
        assert recognizer.ambient_duration == 0.5

    def test_set_language(self):
        """Test changing language."""
        recognizer = SpeechRecognizer()
        recognizer.set_language("fr-FR")

        assert recognizer.language == "fr-FR"

    def test_custom_mic_manager(self):
        """Test with custom microphone manager."""
        mic_manager = MicrophoneManager(device_name="custom", sample_rate=16000)
        recognizer = SpeechRecognizer(mic_manager=mic_manager)

        assert recognizer.mic_manager.device_name == "custom"
        assert recognizer.mic_manager.sample_rate == 16000
