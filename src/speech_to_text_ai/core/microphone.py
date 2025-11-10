"""Microphone management and device selection."""

from typing import List, Optional

import speech_recognition as sr

from speech_to_text_ai.utils.logger import get_logger

logger = get_logger(__name__)


class MicrophoneManager:
    """Manage microphone devices and configuration."""

    def __init__(self, device_name: str = "default", sample_rate: int = 48000, chunk_size: int = 2048):
        """
        Initialize microphone manager.

        Args:
            device_name: Name of the microphone device
            sample_rate: Audio sample rate in Hz
            chunk_size: Buffer size for audio chunks
        """
        self.device_name = device_name
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self.device_id: Optional[int] = None
        logger.info(f"Initialized MicrophoneManager with device: {device_name}")

    @staticmethod
    def list_microphones() -> List[str]:
        """
        Get list of available microphone devices.

        Returns:
            List of microphone device names
        """
        try:
            mic_list: List[str] = sr.Microphone.list_microphone_names()
            logger.info(f"Found {len(mic_list)} microphone devices")
            return mic_list
        except Exception as e:
            error_msg = str(e)
            if "pyaudio" in error_msg.lower() or "PyAudio" in error_msg:
                logger.warning("PyAudio not installed. Install with: pip install PyAudio")
                logger.warning("Or install audio extras: pip install -e '.[audio]'")
            else:
                logger.error(f"Failed to list microphones: {e}")
            return []

    def find_device_id(self) -> Optional[int]:
        """
        Find device ID for configured microphone name.

        Returns:
            Device ID if found, None otherwise
        """
        mic_list = self.list_microphones()

        for i, microphone_name in enumerate(mic_list):
            if microphone_name == self.device_name:
                self.device_id = i
                logger.info(f"Found device ID {i} for '{self.device_name}'")
                return i

        logger.warning(f"Device '{self.device_name}' not found, using default")
        return None

    def get_microphone(self) -> sr.Microphone:
        """
        Get configured microphone instance.

        Returns:
            SpeechRecognition Microphone object
        """
        if self.device_id is None:
            self.device_id = self.find_device_id()

        if self.device_id is not None:
            return sr.Microphone(
                device_index=self.device_id,
                sample_rate=self.sample_rate,
                chunk_size=self.chunk_size,
            )
        else:
            logger.info("Using default microphone")
            return sr.Microphone()

    def print_devices(self) -> None:
        """Print all available microphone devices."""
        mic_list = self.list_microphones()
        print("\n🎤 Available Microphones:")
        print("=" * 60)

        for i, mic_name in enumerate(mic_list):
            status = "✓ SELECTED" if mic_name == self.device_name else ""
            print(f"  [{i}] {mic_name} {status}")

        print("=" * 60)
        print(f"\nTotal devices: {len(mic_list)}\n")
