"""
🎤 Speech-To-Text AI - CLI Interface

Modern command-line interface for speech recognition.
"""

from pathlib import Path
from typing import Optional

import typer
from rich import print as rprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from speech_to_text_ai import __version__
from speech_to_text_ai.config.settings import get_settings
from speech_to_text_ai.core.microphone import MicrophoneManager
from speech_to_text_ai.core.recognizer import SpeechRecognizer
from speech_to_text_ai.core.speaker import TextToSpeech
from speech_to_text_ai.utils.logger import get_logger, setup_logging

# Initialize CLI app
app = typer.Typer(
    name="speech-to-text-ai",
    help="🎤 Modern Speech Recognition CLI with AI-powered transcription",
    add_completion=True,
    rich_markup_mode="rich",
)

console = Console()
logger = get_logger(__name__)


def version_callback(value: bool) -> None:
    """Show version and exit."""
    if value:
        rprint(f"[bold cyan]🎤 Speech-To-Text AI[/bold cyan] version [bold green]{__version__}[/bold green]")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(  # noqa: ARG001
        None,
        "--version",
        "-v",
        help="Show version and exit",
        callback=version_callback,
        is_eager=True,
    ),
) -> None:
    """🎤 Speech-To-Text AI - Modern speech recognition CLI."""
    pass


@app.command()
def listen(
    language: str = typer.Option("en-US", "--language", "-l", help="Language code (e.g., en-US, tr-TR)"),
    microphone: str = typer.Option("default", "--mic", "-m", help="Microphone device name"),
    timeout: int = typer.Option(15, "--timeout", "-t", help="Listening timeout in seconds"),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Save result to file"),
    verbose: bool = typer.Option(False, "--verbose", help="Enable verbose logging"),
) -> None:
    """
    🎧 Listen once and recognize speech.

    Example:
        speech-to-text-ai listen --language tr-TR
        speech-to-text-ai listen -l en-US -o output.txt
    """
    setup_logging(verbose=verbose)

    # Setup
    mic_manager = MicrophoneManager(device_name=microphone)
    recognizer = SpeechRecognizer(language=language, mic_manager=mic_manager, timeout=timeout)

    # Show configuration
    with console.status("[bold green]Initializing...", spinner="dots"):
        console.print(
            Panel.fit(
                f"[cyan]Language:[/cyan] {language}\n"
                f"[cyan]Microphone:[/cyan] {microphone}\n"
                f"[cyan]Timeout:[/cyan] {timeout}s",
                title="🎤 Configuration",
                border_style="blue",
            )
        )

    # Recognize
    result = recognizer.recognize_once()

    # Display result
    if result.success:
        console.print(f"\n[bold green]✓ Recognized:[/bold green] {result.text}\n")

        # Save to file if requested
        if output:
            output.write_text(result.text)
            console.print(f"[dim]💾 Saved to {output}[/dim]")
    else:
        console.print(f"\n[bold red]✗ Error:[/bold red] {result.error}\n")
        raise typer.Exit(1)


@app.command()
def continuous(
    language: str = typer.Option("en-US", "--language", "-l", help="Language code"),
    microphone: str = typer.Option("default", "--mic", "-m", help="Microphone device name"),
    max_iterations: Optional[int] = typer.Option(None, "--max", help="Maximum recognition iterations"),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Append results to file"),
    verbose: bool = typer.Option(False, "--verbose", help="Enable verbose logging"),
) -> None:
    """
    🔄 Continuous speech recognition mode.

    Listens continuously and recognizes speech until stopped (Ctrl+C).

    Example:
        speech-to-text-ai continuous --language en-US
        speech-to-text-ai continuous -l tr-TR --max 10
    """
    setup_logging(verbose=verbose)

    # Setup
    mic_manager = MicrophoneManager(device_name=microphone)
    recognizer = SpeechRecognizer(language=language, mic_manager=mic_manager)

    # Show configuration
    console.print(
        Panel.fit(
            f"[cyan]Language:[/cyan] {language}\n"
            f"[cyan]Microphone:[/cyan] {microphone}\n"
            f"[cyan]Max iterations:[/cyan] {max_iterations or '∞'}",
            title="🔄 Continuous Mode",
            border_style="blue",
        )
    )
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Callback to save results
    def save_callback(result):
        if output and result.success:
            with output.open("a") as f:
                f.write(result.text + "\n")

    # Start continuous recognition
    try:
        recognizer.recognize_continuous(max_iterations=max_iterations, callback=save_callback if output else None)
    except KeyboardInterrupt:
        console.print("\n[yellow]⏹️  Stopped by user[/yellow]")


@app.command()
def interactive(
    language: str = typer.Option("en-US", "--language", "-l", help="Language code"),
    microphone: str = typer.Option("default", "--mic", "-m", help="Microphone device name"),
    verbose: bool = typer.Option(False, "--verbose", help="Enable verbose logging"),
) -> None:
    """
    💬 Interactive voice assistant mode.

    Recognizes speech and speaks it back using text-to-speech.

    Example:
        speech-to-text-ai interactive --language en-US
    """
    setup_logging(verbose=verbose)

    # Setup
    mic_manager = MicrophoneManager(device_name=microphone)
    recognizer = SpeechRecognizer(language=language, mic_manager=mic_manager)
    tts = TextToSpeech()

    # Show configuration
    console.print(
        Panel.fit(
            f"[cyan]Language:[/cyan] {language}\n" f"[cyan]Microphone:[/cyan] {microphone}",
            title="💬 Interactive Mode",
            border_style="blue",
        )
    )
    console.print("[dim]Press Ctrl+C to stop[/dim]\n")

    # Main loop
    try:
        while True:
            result = recognizer.recognize_once(show_prompt=False)

            if result.success:
                console.print(f"[green]✓[/green] You: {result.text}")
                console.print(f"[blue]🔊[/blue] AI: {result.text}")
                tts.speak(result.text)
            else:
                console.print(f"[red]✗[/red] {result.error}")

    except KeyboardInterrupt:
        console.print("\n[yellow]⏹️  Stopped by user[/yellow]")


@app.command()
def devices(
    detailed: bool = typer.Option(False, "--detailed", "-d", help="Show detailed information"),
) -> None:
    """
    🎙️ List available microphone devices.

    Example:
        speech-to-text-ai devices
        speech-to-text-ai devices --detailed
    """
    mic_manager = MicrophoneManager()
    mic_list = mic_manager.list_microphones()

    # Create table
    table = Table(title="🎙️ Available Microphones", show_header=True, header_style="bold cyan")
    table.add_column("ID", style="dim", width=6)
    table.add_column("Device Name", style="white")

    if detailed:
        table.add_column("Status", style="green")

    for i, mic_name in enumerate(mic_list):
        if detailed:
            table.add_row(str(i), mic_name, "✓ Available")
        else:
            table.add_row(str(i), mic_name)

    console.print(table)
    console.print(f"\n[dim]Total: {len(mic_list)} devices[/dim]")


@app.command()
def languages(
    search: Optional[str] = typer.Option(None, "--search", "-s", help="Search for language"),
) -> None:
    """
    🌍 List supported languages.

    Example:
        speech-to-text-ai languages
        speech-to-text-ai languages --search turkish
    """
    settings = get_settings()

    # Create table
    table = Table(title="🌍 Supported Languages", show_header=True, header_style="bold cyan")
    table.add_column("Short Code", style="yellow", width=12)
    table.add_column("Full Code", style="cyan", width=15)
    table.add_column("Language", style="white")

    # Language names
    lang_names = {
        "en": "English",
        "tr": "Turkish (Türkçe)",
        "es": "Spanish (Español)",
        "fr": "French (Français)",
        "de": "German (Deutsch)",
        "it": "Italian (Italiano)",
        "pt": "Portuguese (Português)",
        "ru": "Russian (Русский)",
        "ja": "Japanese (日本語)",
        "ko": "Korean (한국어)",
        "zh": "Chinese (中文)",
        "ar": "Arabic (العربية)",
    }

    # Filter if search provided
    for short_code, full_code in sorted(settings.languages.items()):
        lang_name = lang_names.get(short_code, short_code.upper())

        if search and search.lower() not in lang_name.lower():
            continue

        table.add_row(short_code, full_code, lang_name)

    console.print(table)


@app.command()
def config(
    show: bool = typer.Option(False, "--show", help="Show current configuration"),
    save: bool = typer.Option(False, "--save", help="Save current configuration"),
    config_file: Path = typer.Option(
        Path.home() / ".config" / "speech-to-text-ai" / "config.json",
        "--file",
        "-f",
        help="Config file path",
    ),
) -> None:
    """
    ⚙️ Manage configuration.

    Example:
        speech-to-text-ai config --show
        speech-to-text-ai config --save
    """
    settings = get_settings(config_file if config_file.exists() else None)

    if show:
        table = Table(title="⚙️ Current Configuration", show_header=True, header_style="bold cyan")
        table.add_column("Setting", style="cyan")
        table.add_column("Value", style="white")

        table.add_row("Microphone", settings.microphone_name)
        table.add_row("Sample Rate", f"{settings.sample_rate} Hz")
        table.add_row("Chunk Size", str(settings.chunk_size))
        table.add_row("Language", settings.language)
        table.add_row("Timeout", f"{settings.timeout}s")
        table.add_row("TTS Rate", f"{settings.tts_rate} wpm")
        table.add_row("TTS Volume", f"{settings.tts_volume}")
        table.add_row("Log Level", settings.log_level)

        console.print(table)

    if save:
        settings.save(config_file)
        console.print(f"[green]✓[/green] Configuration saved to {config_file}")


if __name__ == "__main__":
    app()
