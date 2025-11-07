"""Tests for text-to-speech."""

import pytest
from speech_to_text_ai.core.speaker import TextToSpeech


class TestTextToSpeech:
    """Test TextToSpeech class."""

    def test_initialization(self):
        """Test TTS initialization."""
        tts = TextToSpeech(rate=200, volume=0.8)

        assert tts.rate == 200
        assert tts.volume == 0.8
        assert tts.engine is None  # Not initialized until first use

    def test_default_initialization(self):
        """Test TTS with defaults."""
        tts = TextToSpeech()

        assert tts.rate == 150
        assert tts.volume == 1.0

    def test_set_rate(self):
        """Test setting speech rate."""
        tts = TextToSpeech()
        tts.set_rate(180)

        assert tts.rate == 180

    def test_set_volume(self):
        """Test setting volume."""
        tts = TextToSpeech()
        tts.set_volume(0.5)

        assert tts.volume == 0.5

    def test_volume_bounds(self):
        """Test volume is bounded between 0 and 1."""
        tts = TextToSpeech()

        tts.set_volume(1.5)
        assert tts.volume == 1.0

        tts.set_volume(-0.5)
        assert tts.volume == 0.0
