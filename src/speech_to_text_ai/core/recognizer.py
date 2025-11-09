"""Speech recognition core functionality."""

from typing import Any, Callable, Dict, Optional

import speech_recognition as sr

from speech_to_text_ai.core.microphone import MicrophoneManager
from speech_to_text_ai.utils.logger import get_logger

logger = get_logger(__name__)


class RecognitionResult:
    """Container for speech recognition results."""

    def __init__(
        self,
        text: Optional[str] = None,
        success: bool = False,
        error: Optional[str] = None,
        confidence: Optional[float] = None,
    ):
        """
        Initialize recognition result.

        Args:
            text: Recognized text
            success: Whether recognition was successful
            error: Error message if failed
            confidence: Confidence score (0.0 to 1.0)
        """
        self.text = text
        self.success = success
        self.error = error
        self.confidence = confidence

    def to_dict(self) -> Dict[str, Any]:
        """Convert result to dictionary."""
        return {
            "text": self.text,
            "success": self.success,
            "error": self.error,
            "confidence": self.confidence,
        }

    def __str__(self) -> str:
        """String representation."""
        if self.success:
            return f"✓ {self.text}"
        else:
            return f"✗ {self.error}"


class SpeechRecognizer:
    """Main speech recognition engine."""

    def __init__(
        self,
        language: str = "en-US",
        mic_manager: Optional[MicrophoneManager] = None,
        timeout: int = 15,
        ambient_duration: float = 0.5,
    ):
        """
        Initialize speech recognizer.

        Args:
            language: Language code (e.g., 'en-US', 'tr-TR')
            mic_manager: MicrophoneManager instance
            timeout: Maximum time to wait for speech (seconds)
            ambient_duration: Time to adjust for ambient noise (seconds)
        """
        self.language = language
        self.mic_manager = mic_manager or MicrophoneManager()
        self.timeout = timeout
        self.ambient_duration = ambient_duration
        self.recognizer = sr.Recognizer()
        logger.info(f"Initialized SpeechRecognizer (language={language})")

    def recognize_once(self, show_prompt: bool = True) -> RecognitionResult:
        """
        Recognize speech once from microphone.

        Args:
            show_prompt: Whether to show listening prompt

        Returns:
            RecognitionResult with recognized text or error
        """
        try:
            microphone = self.mic_manager.get_microphone()

            with microphone as source:
                # Adjust for ambient noise
                logger.debug("Adjusting for ambient noise...")
                self.recognizer.adjust_for_ambient_noise(source, duration=self.ambient_duration)

                # Listen for speech
                if show_prompt:
                    print("🎤 Listening... (speak now)")

                logger.debug(f"Listening with timeout={self.timeout}s")
                audio = self.recognizer.listen(source, timeout=self.timeout)

                if show_prompt:
                    print("⏳ Processing...")

            # Recognize speech using Google Speech Recognition
            logger.debug("Recognizing speech...")
            text = self.recognizer.recognize_google(audio, language=self.language)

            logger.info(f"Recognized: {text}")
            return RecognitionResult(text=text, success=True)

        except sr.WaitTimeoutError:
            error_msg = "No speech detected (timeout)"
            logger.warning(error_msg)
            return RecognitionResult(success=False, error=error_msg)

        except sr.UnknownValueError:
            error_msg = "Could not understand audio"
            logger.warning(error_msg)
            return RecognitionResult(success=False, error=error_msg)

        except sr.RequestError as e:
            error_msg = f"API error: {e}"
            logger.error(error_msg)
            return RecognitionResult(success=False, error=error_msg)

        except Exception as e:
            error_msg = f"Unexpected error: {e}"
            logger.error(error_msg)
            return RecognitionResult(success=False, error=error_msg)

    def recognize_continuous(
        self,
        max_iterations: Optional[int] = None,
        callback: Optional[Callable[[Any], None]] = None,
    ) -> None:
        """
        Continuously recognize speech until stopped.

        Args:
            max_iterations: Maximum number of recognitions (None = infinite)
            callback: Optional callback function(result: RecognitionResult)
        """
        iteration = 0
        logger.info("Starting continuous recognition")
        print("\n🎙️  Continuous Recognition Mode")
        print("=" * 60)
        print("Speak naturally. Press Ctrl+C to stop.\n")

        try:
            while max_iterations is None or iteration < max_iterations:
                result = self.recognize_once(show_prompt=False)

                if result.success:
                    print(f"✓ You said: {result.text}")
                else:
                    print(f"✗ {result.error}")

                if callback:
                    callback(result)

                iteration += 1

        except KeyboardInterrupt:
            print("\n\n⏹️  Stopped by user")
            logger.info("Continuous recognition stopped by user")
        except Exception as e:
            logger.error(f"Continuous recognition error: {e}")
            raise

    def set_language(self, language: str) -> None:
        """
        Change recognition language.

        Args:
            language: Language code (e.g., 'en-US', 'tr-TR')
        """
        self.language = language
        logger.info(f"Language changed to {language}")
