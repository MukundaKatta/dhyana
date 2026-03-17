"""Meditation timer with bell intervals and ambient descriptions."""

import time
from typing import Optional, Callable

from dhyana.models import MeditationStyle


# Ambient descriptions for different meditation settings
AMBIENT_DESCRIPTIONS: dict[str, str] = {
    "forest": (
        "You are seated in a quiet forest clearing. Sunlight filters through "
        "the canopy above, creating dappled patterns on the ground. "
        "Birds sing softly in the distance. The scent of pine and earth "
        "surrounds you. A gentle breeze rustles the leaves."
    ),
    "mountain": (
        "You sit on a mountain summit at dawn. The air is crisp and clear. "
        "Clouds drift below you like a sea of white. The sky deepens from "
        "indigo to gold as the sun rises. Silence stretches in every direction."
    ),
    "ocean": (
        "You are on a quiet beach. Waves roll in with a steady rhythm, "
        "advancing and retreating. The sand beneath you is warm. "
        "Salt air fills your lungs. Seabirds wheel overhead."
    ),
    "garden": (
        "You sit in a serene Japanese garden. A stone lantern stands nearby. "
        "Raked gravel patterns surround you. A small stream trickles over stones. "
        "Cherry blossoms drift in the still air."
    ),
    "temple": (
        "You are inside a quiet temple. The air is cool and still. "
        "Incense smoke curls upward in thin spirals. "
        "Candlelight flickers on ancient stone walls. "
        "Deep silence holds everything."
    ),
    "meadow": (
        "You rest in a wide meadow of tall grass and wildflowers. "
        "Bees hum lazily among the blossoms. The sky above is vast and blue. "
        "The grass sways gently. Warmth soaks into your skin."
    ),
    "rain": (
        "You sit by a window as rain falls steadily outside. "
        "Each drop taps the glass with a soft rhythm. "
        "The world is muted and gray, cocooned in gentle sound. "
        "Inside, you are warm, dry, and safe."
    ),
    "night_sky": (
        "You lie beneath a vast night sky. Stars scatter across the darkness "
        "in uncountable numbers. The Milky Way arches overhead. "
        "The air is cool and still. You are small, held by something immense."
    ),
}


class BellConfig:
    """Configuration for meditation bell intervals."""

    def __init__(
        self,
        start_bells: int = 3,
        end_bells: int = 3,
        interval_bells: int = 0,
        interval_minutes: int = 5,
    ) -> None:
        self.start_bells = start_bells
        self.end_bells = end_bells
        self.interval_bells = interval_bells
        self.interval_minutes = interval_minutes


class MeditationTimer:
    """Timer for meditation sessions with bell intervals and ambient settings."""

    def __init__(self, bell_config: Optional[BellConfig] = None) -> None:
        self._bell_config = bell_config or BellConfig()
        self._is_running = False
        self._elapsed_seconds = 0
        self._duration_minutes = 0

    @property
    def is_running(self) -> bool:
        """Return whether the timer is currently running."""
        return self._is_running

    @property
    def elapsed_seconds(self) -> int:
        """Return elapsed seconds."""
        return self._elapsed_seconds

    @property
    def elapsed_minutes(self) -> float:
        """Return elapsed time in minutes."""
        return self._elapsed_seconds / 60.0

    @property
    def remaining_seconds(self) -> int:
        """Return remaining seconds."""
        total = self._duration_minutes * 60
        return max(0, total - self._elapsed_seconds)

    @property
    def bell_config(self) -> BellConfig:
        """Return the bell configuration."""
        return self._bell_config

    def set_duration(self, minutes: int) -> None:
        """Set the meditation duration in minutes."""
        self._duration_minutes = minutes

    def set_bell_config(self, config: BellConfig) -> None:
        """Set the bell configuration."""
        self._bell_config = config

    def start(self) -> dict[str, str]:
        """Start the timer and return session start info."""
        self._is_running = True
        self._elapsed_seconds = 0
        bells = "ring " * self._bell_config.start_bells
        return {
            "status": "started",
            "duration": f"{self._duration_minutes} minutes",
            "bells": bells.strip(),
            "message": f"Meditation timer started for {self._duration_minutes} minutes.",
        }

    def stop(self) -> dict[str, str]:
        """Stop the timer and return session summary."""
        self._is_running = False
        bells = "ring " * self._bell_config.end_bells
        return {
            "status": "completed",
            "elapsed": f"{self.elapsed_minutes:.1f} minutes",
            "bells": bells.strip(),
            "message": f"Session complete. You meditated for {self.elapsed_minutes:.1f} minutes.",
        }

    def tick(self, seconds: int = 1) -> Optional[str]:
        """Advance the timer by the given seconds. Returns bell event if interval is hit."""
        if not self._is_running:
            return None

        self._elapsed_seconds += seconds

        if self._elapsed_seconds >= self._duration_minutes * 60:
            self._is_running = False
            return "session_complete"

        if (
            self._bell_config.interval_bells > 0
            and self._bell_config.interval_minutes > 0
        ):
            interval_seconds = self._bell_config.interval_minutes * 60
            if (
                self._elapsed_seconds % interval_seconds == 0
                and self._elapsed_seconds > 0
            ):
                return "interval_bell"

        return None

    def get_progress(self) -> dict[str, float]:
        """Return progress information."""
        total = self._duration_minutes * 60 if self._duration_minutes else 1
        return {
            "elapsed_minutes": round(self._elapsed_seconds / 60, 1),
            "remaining_minutes": round(max(0, (total - self._elapsed_seconds)) / 60, 1),
            "percent_complete": round(min(100, (self._elapsed_seconds / total) * 100), 1),
        }

    def get_ambient_description(self, setting: str = "forest") -> str:
        """Get an ambient description for the meditation setting."""
        return AMBIENT_DESCRIPTIONS.get(
            setting,
            AMBIENT_DESCRIPTIONS["forest"],
        )

    @staticmethod
    def available_ambients() -> list[str]:
        """Return all available ambient settings."""
        return list(AMBIENT_DESCRIPTIONS.keys())

    def format_time(self, seconds: Optional[int] = None) -> str:
        """Format seconds as MM:SS."""
        secs = seconds if seconds is not None else self._elapsed_seconds
        minutes = secs // 60
        remaining_secs = secs % 60
        return f"{minutes:02d}:{remaining_secs:02d}"
