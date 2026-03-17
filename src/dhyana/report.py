"""Rich console reporting for Dhyana."""

from typing import Optional

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn
from rich.text import Text

from dhyana.models import (
    Session, Technique, GuidedScript, MeditationStyle,
    MoodState, Milestone, MilestoneType,
)

console = Console()


def display_technique(technique: Technique) -> None:
    """Display a meditation technique with full details."""
    content_parts = [
        f"[italic]{technique.description}[/]",
        "",
        "[bold]Instructions:[/]",
    ]
    for i, step in enumerate(technique.instructions, 1):
        content_parts.append(f"  {i}. {step}")

    content_parts.append("")
    content_parts.append("[bold]Benefits:[/]")
    for benefit in technique.benefits:
        content_parts.append(f"  - {benefit}")

    if technique.tips:
        content_parts.append("")
        content_parts.append("[bold]Tips:[/]")
        for tip in technique.tips:
            content_parts.append(f"  - {tip}")

    if technique.origin:
        content_parts.append(f"\n[dim]Origin: {technique.origin}[/]")

    difficulty_colors = {
        "beginner": "green",
        "intermediate": "yellow",
        "advanced": "red",
    }
    diff_color = difficulty_colors.get(technique.difficulty.value, "white")
    subtitle = (
        f"[{diff_color}]{technique.difficulty.value.title()}[/] | "
        f"{technique.recommended_duration_minutes} min"
    )

    panel = Panel(
        "\n".join(content_parts),
        title=technique.name,
        subtitle=subtitle,
        border_style="cyan",
        padding=(1, 2),
    )
    console.print(panel)


def display_guided_script(script: GuidedScript) -> None:
    """Display a guided meditation script."""
    console.print()
    console.rule(f"[bold cyan]{script.title}[/]")
    console.print(
        f"[dim]{script.style.value.replace('_', ' ').title()} | "
        f"{script.duration_minutes} min | "
        f"{script.difficulty.value.title()}[/]",
        justify="center",
    )
    console.print()

    console.print(Panel(
        script.introduction,
        title="Introduction",
        border_style="blue",
        padding=(1, 2),
    ))

    for i, segment in enumerate(script.body_segments, 1):
        console.print(Panel(
            segment,
            title=f"Part {i}",
            border_style="dim blue",
            padding=(1, 2),
        ))

    console.print(Panel(
        script.closing,
        title="Closing",
        border_style="green",
        padding=(1, 2),
    ))
    console.print()


def display_session(session: Session) -> None:
    """Display a meditation session summary."""
    parts = [
        f"Technique: {session.technique.value.replace('_', ' ').title()}",
        f"Duration: {session.duration_minutes} minutes",
    ]
    if session.mood_before:
        parts.append(f"Mood Before: {session.mood_before.value.replace('_', ' ').title()}")
    if session.mood_after:
        parts.append(f"Mood After: {session.mood_after.value.replace('_', ' ').title()}")
    if session.mood_improvement is not None:
        imp = session.mood_improvement
        color = "green" if imp > 0 else "red" if imp < 0 else "yellow"
        parts.append(f"Mood Change: [{color}]{imp:+d}[/]")
    if session.notes:
        parts.append(f"Notes: {session.notes}")

    status = "[green]Completed[/]" if session.completed else "[yellow]Partial[/]"
    parts.append(f"Status: {status}")

    panel = Panel(
        "\n".join(parts),
        title=session.timestamp.strftime("%Y-%m-%d %H:%M"),
        border_style="blue",
    )
    console.print(panel)


def display_sessions_table(sessions: list[Session]) -> None:
    """Display multiple sessions in a table."""
    table = Table(title="Meditation Sessions", border_style="blue")
    table.add_column("Date", style="cyan")
    table.add_column("Technique")
    table.add_column("Duration")
    table.add_column("Mood Change")
    table.add_column("Status")

    for session in sessions:
        date_str = session.timestamp.strftime("%Y-%m-%d %H:%M")
        technique = session.technique.value.replace("_", " ").title()
        duration = f"{session.duration_minutes} min"

        imp = session.mood_improvement
        if imp is not None:
            color = "green" if imp > 0 else "red" if imp < 0 else "yellow"
            mood_change = f"[{color}]{imp:+d}[/]"
        else:
            mood_change = "-"

        status = "[green]Done[/]" if session.completed else "[yellow]Partial[/]"
        table.add_row(date_str, technique, duration, mood_change, status)

    console.print(table)


def display_techniques_table(techniques: list[Technique]) -> None:
    """Display techniques in a compact table."""
    table = Table(title="Meditation Techniques", border_style="cyan")
    table.add_column("Name", style="bold")
    table.add_column("Style")
    table.add_column("Difficulty")
    table.add_column("Duration")
    table.add_column("Description", max_width=40)

    difficulty_colors = {"beginner": "green", "intermediate": "yellow", "advanced": "red"}

    for tech in techniques:
        diff_color = difficulty_colors.get(tech.difficulty.value, "white")
        table.add_row(
            tech.name,
            tech.style.value.replace("_", " ").title(),
            f"[{diff_color}]{tech.difficulty.value.title()}[/]",
            f"{tech.recommended_duration_minutes} min",
            tech.description[:40] + "...",
        )

    console.print(table)


def display_stats(stats: dict[str, float | int | str]) -> None:
    """Display meditation statistics."""
    table = Table(title="Meditation Statistics", border_style="blue")
    table.add_column("Metric", style="bold")
    table.add_column("Value", justify="right")

    for key, value in stats.items():
        label = key.replace("_", " ").title()
        if isinstance(value, float):
            table.add_row(label, f"{value:.1f}")
        else:
            table.add_row(label, str(value))

    console.print(table)


def display_progress(summary: dict, milestones: list[Milestone]) -> None:
    """Display progress summary with milestones."""
    console.print()
    console.rule("[bold blue]Meditation Progress[/]")
    console.print()

    # Summary stats
    stats_table = Table(border_style="blue")
    stats_table.add_column("Metric", style="bold")
    stats_table.add_column("Value", justify="right")

    for key, value in summary.items():
        label = key.replace("_", " ").title()
        if isinstance(value, float):
            stats_table.add_row(label, f"{value:.1f}")
        else:
            stats_table.add_row(label, str(value))

    console.print(stats_table)
    console.print()

    # Milestones
    milestone_table = Table(title="Milestones", border_style="yellow")
    milestone_table.add_column("Badge", style="bold")
    milestone_table.add_column("Description")
    milestone_table.add_column("Status")

    for milestone in milestones:
        if milestone.achieved:
            status = "[green]Achieved[/]"
        else:
            status = "[dim]Locked[/]"
        milestone_table.add_row(milestone.name, milestone.description, status)

    console.print(milestone_table)
    console.print()


def display_ambient(description: str, setting_name: str) -> None:
    """Display an ambient meditation setting description."""
    panel = Panel(
        f"[italic]{description}[/]",
        title=f"Setting: {setting_name.replace('_', ' ').title()}",
        border_style="bright_blue",
        padding=(1, 3),
    )
    console.print(panel)


def display_timer_progress(elapsed: float, remaining: float, percent: float) -> None:
    """Display timer progress."""
    console.print(
        f"  Elapsed: {elapsed:.1f} min | "
        f"Remaining: {remaining:.1f} min | "
        f"Progress: {percent:.0f}%"
    )
