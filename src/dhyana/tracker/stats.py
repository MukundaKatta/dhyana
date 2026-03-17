"""Meditation statistics computation."""

from datetime import date, timedelta
from collections import Counter
from statistics import mean, stdev
from typing import Optional

from dhyana.models import Session, MeditationStyle, MoodState
from dhyana.tracker.sessions import SessionTracker


class MeditationStats:
    """Computes meditation statistics including streaks, totals, and consistency."""

    def __init__(self, tracker: Optional[SessionTracker] = None) -> None:
        self._tracker = tracker or SessionTracker()

    @property
    def sessions(self) -> list[Session]:
        """Access sessions from the tracker."""
        return self._tracker.sessions

    def total_time_minutes(self) -> int:
        """Total minutes spent meditating."""
        return self._tracker.total_minutes()

    def total_time_hours(self) -> float:
        """Total hours spent meditating."""
        return round(self._tracker.total_minutes() / 60.0, 1)

    def total_sessions(self) -> int:
        """Total number of sessions."""
        return self._tracker.total_sessions()

    def current_streak(self) -> int:
        """Calculate the current daily meditation streak."""
        if not self.sessions:
            return 0

        dates_practiced = sorted(
            set(s.timestamp.date() for s in self.sessions),
            reverse=True,
        )

        if not dates_practiced:
            return 0

        streak = 0
        expected = date.today()

        for practiced_date in dates_practiced:
            if practiced_date == expected:
                streak += 1
                expected -= timedelta(days=1)
            elif practiced_date < expected:
                break

        return streak

    def longest_streak(self) -> int:
        """Calculate the longest daily meditation streak."""
        if not self.sessions:
            return 0

        dates_practiced = sorted(set(s.timestamp.date() for s in self.sessions))

        if not dates_practiced:
            return 0

        max_streak = 1
        current = 1

        for i in range(1, len(dates_practiced)):
            if dates_practiced[i] - dates_practiced[i - 1] == timedelta(days=1):
                current += 1
                max_streak = max(max_streak, current)
            else:
                current = 1

        return max_streak

    def consistency_score(self, days: int = 30) -> float:
        """Calculate consistency as percentage of days practiced in the last N days.

        Returns a value between 0.0 and 1.0.
        """
        cutoff = date.today() - timedelta(days=days - 1)
        dates_practiced = set(
            s.timestamp.date() for s in self.sessions
            if s.timestamp.date() >= cutoff
        )
        return round(len(dates_practiced) / days, 2)

    def average_session_duration(self) -> float:
        """Average session duration in minutes."""
        return self._tracker.average_duration()

    def sessions_per_week(self, weeks: int = 4) -> float:
        """Average sessions per week over the past N weeks."""
        cutoff = date.today() - timedelta(weeks=weeks)
        recent = [s for s in self.sessions if s.timestamp.date() >= cutoff]
        return round(len(recent) / weeks, 1)

    def technique_distribution(self) -> dict[MeditationStyle, float]:
        """Return percentage distribution of techniques used."""
        total = len(self.sessions)
        if total == 0:
            return {}
        freq = self._tracker.technique_frequency()
        return {
            tech: round(count / total * 100, 1)
            for tech, count in freq.items()
        }

    def unique_techniques_used(self) -> int:
        """Count of unique techniques practiced."""
        return len(set(s.technique for s in self.sessions))

    def time_of_day_preference(self) -> dict[str, int]:
        """Analyze preferred meditation time of day."""
        buckets: dict[str, int] = {
            "morning": 0,
            "afternoon": 0,
            "evening": 0,
            "night": 0,
        }
        for session in self.sessions:
            hour = session.timestamp.hour
            if 5 <= hour < 12:
                buckets["morning"] += 1
            elif 12 <= hour < 17:
                buckets["afternoon"] += 1
            elif 17 <= hour < 21:
                buckets["evening"] += 1
            else:
                buckets["night"] += 1
        return {k: v for k, v in buckets.items() if v > 0}

    def mood_improvement_stats(self) -> dict[str, Optional[float]]:
        """Statistics about mood improvement from meditation."""
        improvements = [
            s.mood_improvement for s in self.sessions
            if s.mood_improvement is not None
        ]
        if not improvements:
            return {
                "average": None,
                "best": None,
                "worst": None,
            }
        return {
            "average": round(mean(improvements), 2),
            "best": max(improvements),
            "worst": min(improvements),
        }

    def weekly_summary(self) -> dict[str, float | int]:
        """Get a summary of the past week."""
        week_sessions = self._tracker.sessions_this_week()
        total_mins = sum(s.duration_minutes for s in week_sessions)

        return {
            "sessions": len(week_sessions),
            "total_minutes": total_mins,
            "average_duration": round(total_mins / len(week_sessions), 1) if week_sessions else 0,
            "unique_techniques": len(set(s.technique for s in week_sessions)),
        }
