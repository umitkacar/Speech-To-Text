"""Tests for microphone management."""

import pytest
from speech_to_text_ai.core.microphone import MicrophoneManager


class TestMicrophoneManager:
    """Test MicrophoneManager class."""

    def test_initialization(self):
        """Test microphone manager initialization."""
        mic_manager = MicrophoneManager(device_name="test", sample_rate=16000, chunk_size=1024)

        assert mic_manager.device_name == "test"
        assert mic_manager.sample_rate == 16000
        assert mic_manager.chunk_size == 1024
        assert mic_manager.device_id is None

    def test_default_initialization(self):
        """Test microphone manager with defaults."""
        mic_manager = MicrophoneManager()

        assert mic_manager.device_name == "default"
        assert mic_manager.sample_rate == 48000
        assert mic_manager.chunk_size == 2048

    def test_list_microphones(self):
        """Test listing microphones."""
        mic_list = MicrophoneManager.list_microphones()

        assert isinstance(mic_list, list)
        # Note: Actual microphones may not be available in test environment

    def test_find_device_id(self):
        """Test finding device ID."""
        mic_manager = MicrophoneManager(device_name="nonexistent")
        device_id = mic_manager.find_device_id()

        # Should return None for nonexistent device
        assert device_id is None

    def test_get_microphone(self):
        """Test getting microphone instance."""
        mic_manager = MicrophoneManager()
        microphone = mic_manager.get_microphone()

        assert microphone is not None
        # Basic check that we got a Microphone object
        assert hasattr(microphone, "__enter__")
        assert hasattr(microphone, "__exit__")
