"""Pydantic models for Dhyana."""

from datetime import datetime, date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class MeditationStyle(str, Enum):
    """Styles of meditation."""
    BREATH_AWARENESS = "breath_awareness"
    BODY_SCAN = "body_scan"
    LOVING_KINDNESS = "loving_kindness"
    VISUALIZATION = "visualization"
    MANTRA = "mantra"
    VIPASSANA = "vipassana"
    ZAZEN = "zazen"
    YOGA_NIDRA = "yoga_nidra"
    TRATAKA = "trataka"
    METTA = "metta"
    MINDFULNESS = "mindfulness"
    WALKING = "walking"
    TRANSCENDENTAL = "transcendental"
    CHAKRA = "chakra"
    SOUND = "sound"
    OPEN_AWARENESS = "open_awareness"


class Difficulty(str, Enum):
    """Difficulty levels for meditation techniques."""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"


class MoodState(str, Enum):
    """Mood states before and after meditation."""
    VERY_STRESSED = "very_stressed"
    STRESSED = "stressed"
    NEUTRAL = "neutral"
    CALM = "calm"
    VERY_CALM = "very_calm"
    PEACEFUL = "peaceful"
    ENERGIZED = "energized"
    SLEEPY = "sleepy"
    FOCUSED = "focused"
    SCATTERED = "scattered"

    @property
    def numeric_value(self) -> int:
        """Convert mood to a numeric scale (1-10)."""
        mapping = {
            MoodState.VERY_STRESSED: 1,
            MoodState.STRESSED: 2,
            MoodState.SCATTERED: 3,
            MoodState.SLEEPY: 4,
            MoodState.NEUTRAL: 5,
            MoodState.CALM: 6,
            MoodState.FOCUSED: 7,
            MoodState.ENERGIZED: 8,
            MoodState.PEACEFUL: 9,
            MoodState.VERY_CALM: 10,
        }
        return mapping.get(self, 5)


class Technique(BaseModel):
    """A meditation technique with instructions."""
    name: str
    style: MeditationStyle
    description: str
    instructions: list[str]
    benefits: list[str]
    difficulty: Difficulty = Difficulty.BEGINNER
    recommended_duration_minutes: int = 10
    origin: str = ""
    tips: list[str] = Field(default_factory=list)


class GuidedScript(BaseModel):
    """A scripted guided meditation session."""
    id: str
    title: str
    style: MeditationStyle
    duration_minutes: int
    introduction: str
    body_segments: list[str]
    closing: str
    difficulty: Difficulty = Difficulty.BEGINNER
    focus_areas: list[str] = Field(default_factory=list)

    @property
    def full_script(self) -> str:
        """Return the complete meditation script."""
        parts = [self.introduction] + self.body_segments + [self.closing]
        return "\n\n".join(parts)

    @property
    def segment_count(self) -> int:
        """Return the number of body segments."""
        return len(self.body_segments)


class Session(BaseModel):
    """A recorded meditation session."""
    id: str = Field(default_factory=lambda: datetime.now().strftime("%Y%m%d%H%M%S"))
    technique: MeditationStyle
    duration_minutes: int = Field(ge=1)
    mood_before: Optional[MoodState] = None
    mood_after: Optional[MoodState] = None
    notes: Optional[str] = None
    guided_script_id: Optional[str] = None
    completed: bool = True
    timestamp: datetime = Field(default_factory=datetime.now)

    @property
    def mood_improvement(self) -> Optional[int]:
        """Calculate mood improvement (positive = better after)."""
        if self.mood_before and self.mood_after:
            return self.mood_after.numeric_value - self.mood_before.numeric_value
        return None


class MilestoneType(str, Enum):
    """Types of milestones."""
    STREAK = "streak"
    TOTAL_TIME = "total_time"
    SESSION_COUNT = "session_count"
    TECHNIQUE_VARIETY = "technique_variety"


class Milestone(BaseModel):
    """A progress milestone or badge."""
    name: str
    description: str
    milestone_type: MilestoneType
    threshold: int
    achieved: bool = False
    achieved_at: Optional[datetime] = None
