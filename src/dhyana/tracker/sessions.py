"""Session tracking for meditation practice."""

from datetime import date, datetime, timedelta
from typing import Optional
from collections import Counter

from dhyana.models import Session, MeditationStyle, MoodState


class SessionTracker:
    """Tracks meditation sessions with duration, technique, and mood."""

    def __init__(self) -> None:
        self._sessions: list[Session] = []

    @property
    def sessions(self) -> list[Session]:
        """Return all tracked sessions."""
        return list(self._sessions)

    def log_session(
        self,
        technique: MeditationStyle,
        duration_minutes: int,
        mood_before: Optional[MoodState] = None,
        mood_after: Optional[MoodState] = None,
        notes: Optional[str] = None,
        guided_script_id: Optional[str] = None,
        completed: bool = True,
    ) -> Session:
        """Log a new meditation session."""
        session = Session(
            technique=technique,
            duration_minutes=duration_minutes,
            mood_before=mood_before,
            mood_after=mood_after,
            notes=notes,
            guided_script_id=guided_script_id,
            completed=completed,
        )
        self._sessions.append(session)
        return session

    def get_sessions_by_date(self, target_date: date) -> list[Session]:
        """Get all sessions for a specific date."""
        return [
            s for s in self._sessions
            if s.timestamp.date() == target_date
        ]

    def get_sessions_in_range(self, start: date, end: date) -> list[Session]:
        """Get sessions within a date range."""
        return [
            s for s in self._sessions
            if start <= s.timestamp.date() <= end
        ]

    def get_sessions_by_technique(self, technique: MeditationStyle) -> list[Session]:
        """Get all sessions using a specific technique."""
        return [s for s in self._sessions if s.technique == technique]

    def get_today_sessions(self) -> list[Session]:
        """Get all sessions from today."""
        return self.get_sessions_by_date(date.today())

    def total_sessions(self) -> int:
        """Return the total number of sessions."""
        return len(self._sessions)

    def total_minutes(self) -> int:
        """Return total minutes meditated."""
        return sum(s.duration_minutes for s in self._sessions)

    def average_duration(self) -> float:
        """Return the average session duration in minutes."""
        if not self._sessions:
            return 0.0
        return self.total_minutes() / len(self._sessions)

    def technique_frequency(self) -> dict[MeditationStyle, int]:
        """Count sessions per technique."""
        counter: Counter[MeditationStyle] = Counter()
        for session in self._sessions:
            counter[session.technique] += 1
        return dict(counter.most_common())

    def favorite_technique(self) -> Optional[MeditationStyle]:
        """Return the most-used technique."""
        freq = self.technique_frequency()
        if not freq:
            return None
        return max(freq, key=freq.get)  # type: ignore

    def average_mood_improvement(self) -> Optional[float]:
        """Calculate average mood improvement across sessions."""
        improvements = [
            s.mood_improvement for s in self._sessions
            if s.mood_improvement is not None
        ]
        if not improvements:
            return None
        return sum(improvements) / len(improvements)

    def best_technique_for_mood(self) -> Optional[MeditationStyle]:
        """Find the technique with the highest average mood improvement."""
        technique_improvements: dict[MeditationStyle, list[int]] = {}
        for session in self._sessions:
            imp = session.mood_improvement
            if imp is not None:
                technique_improvements.setdefault(session.technique, []).append(imp)

        if not technique_improvements:
            return None

        averages = {
            tech: sum(imps) / len(imps)
            for tech, imps in technique_improvements.items()
        }
        return max(averages, key=averages.get)  # type: ignore

    def sessions_this_week(self) -> list[Session]:
        """Get all sessions from the current week."""
        today = date.today()
        week_start = today - timedelta(days=today.weekday())
        return self.get_sessions_in_range(week_start, today)

    def delete_session(self, session_id: str) -> bool:
        """Delete a session by ID."""
        for i, session in enumerate(self._sessions):
            if session.id == session_id:
                self._sessions.pop(i)
                return True
        return False
