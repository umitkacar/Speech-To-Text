"""Application settings and configuration."""

from typing import Optional
from pathlib import Path
from dataclasses import dataclass, field
import json


@dataclass
class Settings:
    """Application settings."""

    # Audio settings
    microphone_name: str = "default"
    sample_rate: int = 48000
    chunk_size: int = 2048

    # Recognition settings
    language: str = "en-US"
    timeout: int = 15
    ambient_duration: float = 0.5

    # TTS settings
    tts_rate: int = 150
    tts_volume: float = 1.0

    # Logging settings
    log_level: str = "INFO"
    log_file: Optional[Path] = None

    # Common languages for quick access
    languages: dict = field(
        default_factory=lambda: {
            "en": "en-US",
            "tr": "tr-TR",
            "es": "es-ES",
            "fr": "fr-FR",
            "de": "de-DE",
            "it": "it-IT",
            "pt": "pt-PT",
            "ru": "ru-RU",
            "ja": "ja-JP",
            "ko": "ko-KR",
            "zh": "zh-CN",
            "ar": "ar-SA",
        }
    )

    @classmethod
    def from_file(cls, config_path: Path) -> "Settings":
        """
        Load settings from JSON file.

        Args:
            config_path: Path to config file

        Returns:
            Settings instance
        """
        if not config_path.exists():
            return cls()

        with open(config_path, "r") as f:
            data = json.load(f)

        return cls(**data)

    def save(self, config_path: Path) -> None:
        """
        Save settings to JSON file.

        Args:
            config_path: Path to save config
        """
        config_path.parent.mkdir(parents=True, exist_ok=True)

        data = {
            "microphone_name": self.microphone_name,
            "sample_rate": self.sample_rate,
            "chunk_size": self.chunk_size,
            "language": self.language,
            "timeout": self.timeout,
            "ambient_duration": self.ambient_duration,
            "tts_rate": self.tts_rate,
            "tts_volume": self.tts_volume,
            "log_level": self.log_level,
        }

        with open(config_path, "w") as f:
            json.dump(data, f, indent=2)

    def get_language_code(self, lang_short: str) -> Optional[str]:
        """
        Get full language code from short code.

        Args:
            lang_short: Short language code (e.g., 'en', 'tr')

        Returns:
            Full language code (e.g., 'en-US', 'tr-TR')
        """
        return self.languages.get(lang_short.lower())


# Global settings instance
_settings: Optional[Settings] = None


def get_settings(config_path: Optional[Path] = None) -> Settings:
    """
    Get global settings instance.

    Args:
        config_path: Optional path to config file

    Returns:
        Settings instance
    """
    global _settings

    if _settings is None:
        if config_path and config_path.exists():
            _settings = Settings.from_file(config_path)
        else:
            _settings = Settings()

    return _settings
