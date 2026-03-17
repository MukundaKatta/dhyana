"""Command-line interface for Dhyana."""

import click
from rich.console import Console

from dhyana.meditation.guided import GuidedMeditation
from dhyana.meditation.timer import MeditationTimer, BellConfig
from dhyana.meditation.techniques import TechniqueLibrary
from dhyana.tracker.sessions import SessionTracker
from dhyana.tracker.stats import MeditationStats
from dhyana.tracker.progress import ProgressTracker
from dhyana.models import MeditationStyle, MoodState, Difficulty
from dhyana import report

console = Console()

# Shared state (in a real app these would be backed by a database)
guided = GuidedMeditation()
technique_lib = TechniqueLibrary()
timer = MeditationTimer()
session_tracker = SessionTracker()
stats = MeditationStats(session_tracker)
progress = ProgressTracker(session_tracker, stats)


@click.group()
@click.version_option(version="0.1.0", prog_name="dhyana")
def cli() -> None:
    """Dhyana - AI Meditation Guide."""
    pass


@cli.command()
@click.option("--style", "-s",
              type=click.Choice([s.value for s in MeditationStyle]),
              default=None, help="Meditation style.")
@click.option("--duration", "-d", type=int, default=None,
              help="Maximum duration in minutes.")
def meditate(style: str | None, duration: int | None) -> None:
    """Start a guided meditation session."""
    if style:
        med_style = MeditationStyle(style)
        scripts = guided.get_by_style(med_style)
    elif duration:
        scripts = guided.get_by_duration(duration)
    else:
        scripts = guided.scripts

    if not scripts:
        console.print("[yellow]No sessions found matching your criteria.[/]")
        return

    import random
    script = random.choice(scripts)
    report.display_guided_script(script)


@cli.command()
@click.option("--difficulty", "-d",
              type=click.Choice([d.value for d in Difficulty]),
              default=None, help="Filter by difficulty.")
@click.option("--search", "-s", type=str, default=None,
              help="Search techniques by keyword.")
def techniques(difficulty: str | None, search: str | None) -> None:
    """Browse meditation techniques."""
    if search:
        techs = technique_lib.search(search)
    elif difficulty:
        techs = technique_lib.get_by_difficulty(Difficulty(difficulty))
    else:
        techs = technique_lib.techniques

    if not techs:
        console.print("[yellow]No techniques found.[/]")
        return

    report.display_techniques_table(techs)


@cli.command()
@click.argument("name")
def technique(name: str) -> None:
    """View details of a specific technique."""
    tech = technique_lib.get_by_name(name)
    if not tech:
        console.print(f"[yellow]Technique '{name}' not found.[/]")
        return
    report.display_technique(tech)


@cli.command(name="timer")
@click.option("--duration", "-d", type=int, default=10,
              help="Duration in minutes.")
@click.option("--ambient", "-a", type=str, default="forest",
              help="Ambient setting.")
@click.option("--bells", "-b", type=int, default=0,
              help="Interval bells every N minutes.")
def timer_cmd(duration: int, ambient: str, bells: int) -> None:
    """Start a meditation timer."""
    description = timer.get_ambient_description(ambient)
    report.display_ambient(description, ambient)

    bell_config = BellConfig(interval_bells=1 if bells > 0 else 0, interval_minutes=bells)
    timer.set_bell_config(bell_config)
    timer.set_duration(duration)

    result = timer.start()
    console.print(f"\n[green]{result['message']}[/]\n")


@cli.command()
def history() -> None:
    """View session history."""
    sessions = session_tracker.sessions
    if not sessions:
        console.print("[yellow]No sessions recorded yet.[/]")
        return
    report.display_sessions_table(sessions)


@cli.command(name="stats")
def stats_cmd() -> None:
    """View meditation statistics."""
    summary = progress.progress_summary()
    milestones = progress.milestones
    report.display_progress(summary, milestones)


@cli.command()
def ambients() -> None:
    """List available ambient settings."""
    settings = timer.available_ambients()
    for setting in settings:
        desc = timer.get_ambient_description(setting)
        report.display_ambient(desc, setting)


if __name__ == "__main__":
    cli()
