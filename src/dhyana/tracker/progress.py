"""Progress tracking with milestone badges."""

from datetime import datetime
from typing import Optional

from dhyana.models import Milestone, MilestoneType, Session, MeditationStyle
from dhyana.tracker.sessions import SessionTracker
from dhyana.tracker.stats import MeditationStats


# Milestone definitions
MILESTONES: list[Milestone] = [
    # Streak milestones
    Milestone(
        name="First Step",
        description="Meditate for your first day",
        milestone_type=MilestoneType.STREAK,
        threshold=1,
    ),
    Milestone(
        name="Three Day Flow",
        description="Maintain a 3-day meditation streak",
        milestone_type=MilestoneType.STREAK,
        threshold=3,
    ),
    Milestone(
        name="Week Warrior",
        description="Maintain a 7-day meditation streak",
        milestone_type=MilestoneType.STREAK,
        threshold=7,
    ),
    Milestone(
        name="Fortnight Focus",
        description="Maintain a 14-day meditation streak",
        milestone_type=MilestoneType.STREAK,
        threshold=14,
    ),
    Milestone(
        name="Monthly Master",
        description="Maintain a 30-day meditation streak",
        milestone_type=MilestoneType.STREAK,
        threshold=30,
    ),
    Milestone(
        name="Century Sitter",
        description="Maintain a 100-day meditation streak",
        milestone_type=MilestoneType.STREAK,
        threshold=100,
    ),

    # Total time milestones
    Milestone(
        name="First Hour",
        description="Accumulate 1 hour of total meditation time",
        milestone_type=MilestoneType.TOTAL_TIME,
        threshold=60,
    ),
    Milestone(
        name="Five Hours Deep",
        description="Accumulate 5 hours of total meditation time",
        milestone_type=MilestoneType.TOTAL_TIME,
        threshold=300,
    ),
    Milestone(
        name="Ten Hour Milestone",
        description="Accumulate 10 hours of total meditation time",
        milestone_type=MilestoneType.TOTAL_TIME,
        threshold=600,
    ),
    Milestone(
        name="Day of Silence",
        description="Accumulate 24 hours of total meditation time",
        milestone_type=MilestoneType.TOTAL_TIME,
        threshold=1440,
    ),
    Milestone(
        name="Hundred Hours",
        description="Accumulate 100 hours of total meditation time",
        milestone_type=MilestoneType.TOTAL_TIME,
        threshold=6000,
    ),

    # Session count milestones
    Milestone(
        name="Beginner Mind",
        description="Complete your first meditation session",
        milestone_type=MilestoneType.SESSION_COUNT,
        threshold=1,
    ),
    Milestone(
        name="Building Habit",
        description="Complete 10 meditation sessions",
        milestone_type=MilestoneType.SESSION_COUNT,
        threshold=10,
    ),
    Milestone(
        name="Dedicated Practitioner",
        description="Complete 50 meditation sessions",
        milestone_type=MilestoneType.SESSION_COUNT,
        threshold=50,
    ),
    Milestone(
        name="Seasoned Meditator",
        description="Complete 100 meditation sessions",
        milestone_type=MilestoneType.SESSION_COUNT,
        threshold=100,
    ),
    Milestone(
        name="Thousand Sessions",
        description="Complete 1000 meditation sessions",
        milestone_type=MilestoneType.SESSION_COUNT,
        threshold=1000,
    ),

    # Technique variety milestones
    Milestone(
        name="Explorer",
        description="Try 3 different meditation techniques",
        milestone_type=MilestoneType.TECHNIQUE_VARIETY,
        threshold=3,
    ),
    Milestone(
        name="Versatile Meditator",
        description="Try 5 different meditation techniques",
        milestone_type=MilestoneType.TECHNIQUE_VARIETY,
        threshold=5,
    ),
    Milestone(
        name="Renaissance Practitioner",
        description="Try 10 different meditation techniques",
        milestone_type=MilestoneType.TECHNIQUE_VARIETY,
        threshold=10,
    ),
]


class ProgressTracker:
    """Tracks meditation progress and awards milestone badges."""

    def __init__(
        self,
        tracker: Optional[SessionTracker] = None,
        stats: Optional[MeditationStats] = None,
    ) -> None:
        self._tracker = tracker or SessionTracker()
        self._stats = stats or MeditationStats(self._tracker)
        self._milestones = [m.model_copy() for m in MILESTONES]

    @property
    def milestones(self) -> list[Milestone]:
        """Return all milestones."""
        return list(self._milestones)

    @property
    def achieved_milestones(self) -> list[Milestone]:
        """Return only achieved milestones."""
        return [m for m in self._milestones if m.achieved]

    @property
    def pending_milestones(self) -> list[Milestone]:
        """Return milestones not yet achieved."""
        return [m for m in self._milestones if not m.achieved]

    def check_milestones(self) -> list[Milestone]:
        """Check all milestones and return newly achieved ones."""
        newly_achieved = []

        current_streak = self._stats.current_streak()
        total_minutes = self._stats.total_time_minutes()
        total_sessions = self._stats.total_sessions()
        unique_techniques = self._stats.unique_techniques_used()

        for milestone in self._milestones:
            if milestone.achieved:
                continue

            value = 0
            if milestone.milestone_type == MilestoneType.STREAK:
                value = current_streak
            elif milestone.milestone_type == MilestoneType.TOTAL_TIME:
                value = total_minutes
            elif milestone.milestone_type == MilestoneType.SESSION_COUNT:
                value = total_sessions
            elif milestone.milestone_type == MilestoneType.TECHNIQUE_VARIETY:
                value = unique_techniques

            if value >= milestone.threshold:
                milestone.achieved = True
                milestone.achieved_at = datetime.now()
                newly_achieved.append(milestone)

        return newly_achieved

    def next_milestone(self) -> Optional[Milestone]:
        """Get the next closest milestone to achieve."""
        pending = self.pending_milestones
        if not pending:
            return None

        current_streak = self._stats.current_streak()
        total_minutes = self._stats.total_time_minutes()
        total_sessions = self._stats.total_sessions()
        unique_techniques = self._stats.unique_techniques_used()

        def distance(m: Milestone) -> float:
            if m.milestone_type == MilestoneType.STREAK:
                return max(0, m.threshold - current_streak) / m.threshold
            elif m.milestone_type == MilestoneType.TOTAL_TIME:
                return max(0, m.threshold - total_minutes) / m.threshold
            elif m.milestone_type == MilestoneType.SESSION_COUNT:
                return max(0, m.threshold - total_sessions) / m.threshold
            elif m.milestone_type == MilestoneType.TECHNIQUE_VARIETY:
                return max(0, m.threshold - unique_techniques) / m.threshold
            return 1.0

        return min(pending, key=distance)

    def progress_summary(self) -> dict[str, int | float | str]:
        """Generate a progress summary."""
        self.check_milestones()
        next_ms = self.next_milestone()
        return {
            "total_sessions": self._stats.total_sessions(),
            "total_hours": self._stats.total_time_hours(),
            "current_streak": self._stats.current_streak(),
            "longest_streak": self._stats.longest_streak(),
            "consistency_30d": self._stats.consistency_score(30),
            "milestones_achieved": len(self.achieved_milestones),
            "milestones_total": len(self._milestones),
            "next_milestone": next_ms.name if next_ms else "All achieved!",
        }

    def get_milestone_progress(self, milestone: Milestone) -> float:
        """Get progress toward a specific milestone as a percentage."""
        if milestone.achieved:
            return 100.0

        if milestone.milestone_type == MilestoneType.STREAK:
            current = self._stats.current_streak()
        elif milestone.milestone_type == MilestoneType.TOTAL_TIME:
            current = self._stats.total_time_minutes()
        elif milestone.milestone_type == MilestoneType.SESSION_COUNT:
            current = self._stats.total_sessions()
        elif milestone.milestone_type == MilestoneType.TECHNIQUE_VARIETY:
            current = self._stats.unique_techniques_used()
        else:
            current = 0

        return round(min(100.0, (current / milestone.threshold) * 100), 1)
