"""Tests for configuration."""

from speech_to_text_ai.config.settings import Settings


class TestSettings:
    """Test Settings class."""

    def test_default_settings(self):
        """Test default settings."""
        settings = Settings()

        assert settings.microphone_name == "default"
        assert settings.sample_rate == 48000
        assert settings.language == "en-US"
        assert settings.timeout == 15
        assert settings.tts_rate == 150

    def test_custom_settings(self):
        """Test custom settings."""
        settings = Settings(language="tr-TR", timeout=20, tts_rate=180)

        assert settings.language == "tr-TR"
        assert settings.timeout == 20
        assert settings.tts_rate == 180

    def test_get_language_code(self):
        """Test getting language code."""
        settings = Settings()

        assert settings.get_language_code("en") == "en-US"
        assert settings.get_language_code("tr") == "tr-TR"
        assert settings.get_language_code("fr") == "fr-FR"
        assert settings.get_language_code("nonexistent") is None

    def test_save_and_load(self, tmp_path):
        """Test saving and loading settings."""
        config_file = tmp_path / "config.json"

        # Create and save settings
        settings = Settings(language="es-ES", timeout=10)
        settings.save(config_file)

        # Verify file exists
        assert config_file.exists()

        # Load settings
        loaded_settings = Settings.from_file(config_file)

        assert loaded_settings.language == "es-ES"
        assert loaded_settings.timeout == 10

    def test_load_nonexistent_file(self, tmp_path):
        """Test loading from nonexistent file returns defaults."""
        config_file = tmp_path / "nonexistent.json"
        settings = Settings.from_file(config_file)

        assert settings.language == "en-US"
        assert settings.microphone_name == "default"
