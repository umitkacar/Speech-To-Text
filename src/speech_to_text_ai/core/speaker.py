"""Text-to-speech functionality."""

from typing import Optional

import pyttsx3

from speech_to_text_ai.utils.logger import get_logger

logger = get_logger(__name__)


class TextToSpeech:
    """Handle text-to-speech conversion."""

    def __init__(self, rate: int = 150, volume: float = 1.0):
        """
        Initialize text-to-speech engine.

        Args:
            rate: Speech rate (words per minute)
            volume: Volume level (0.0 to 1.0)
        """
        self.rate = rate
        self.volume = volume
        self.engine: Optional[pyttsx3.Engine] = None
        logger.info("Initialized TextToSpeech")

    def _init_engine(self) -> None:
        """Initialize the pyttsx3 engine."""
        if self.engine is None:
            try:
                self.engine = pyttsx3.init()
                self.engine.setProperty("rate", self.rate)
                self.engine.setProperty("volume", self.volume)
                logger.info(f"TTS engine initialized (rate={self.rate}, volume={self.volume})")
            except Exception as e:
                logger.error(f"Failed to initialize TTS engine: {e}")
                raise

    def speak(self, text: str) -> None:
        """
        Convert text to speech and play it.

        Args:
            text: Text to speak
        """
        if not text:
            logger.warning("Empty text provided to speak()")
            return

        try:
            self._init_engine()
            if self.engine:
                logger.debug(f"Speaking: {text}")
                self.engine.say(text)
                self.engine.runAndWait()
        except Exception as e:
            logger.error(f"Failed to speak text: {e}")

    def set_rate(self, rate: int) -> None:
        """
        Set speech rate.

        Args:
            rate: Words per minute
        """
        self.rate = rate
        if self.engine:
            self.engine.setProperty("rate", rate)
            logger.info(f"Speech rate set to {rate}")

    def set_volume(self, volume: float) -> None:
        """
        Set speech volume.

        Args:
            volume: Volume level (0.0 to 1.0)
        """
        self.volume = max(0.0, min(1.0, volume))
        if self.engine:
            self.engine.setProperty("volume", self.volume)
            logger.info(f"Volume set to {self.volume}")
