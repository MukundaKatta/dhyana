"""Tests for Dhyana models."""

from dhyana.models import (
    Session, Technique, GuidedScript, MeditationStyle,
    Difficulty, MoodState, Milestone, MilestoneType,
)


class TestSession:
    def test_create_session(self):
        session = Session(
            technique=MeditationStyle.BREATH_AWARENESS,
            duration_minutes=15,
        )
        assert session.technique == MeditationStyle.BREATH_AWARENESS
        assert session.duration_minutes == 15
        assert session.completed is True

    def test_mood_improvement(self):
        session = Session(
            technique=MeditationStyle.METTA,
            duration_minutes=20,
            mood_before=MoodState.STRESSED,
            mood_after=MoodState.CALM,
        )
        assert session.mood_improvement is not None
        assert session.mood_improvement > 0

    def test_mood_improvement_none(self):
        session = Session(
            technique=MeditationStyle.ZAZEN,
            duration_minutes=25,
        )
        assert session.mood_improvement is None


class TestMoodState:
    def test_numeric_values(self):
        assert MoodState.VERY_STRESSED.numeric_value == 1
        assert MoodState.NEUTRAL.numeric_value == 5
        assert MoodState.VERY_CALM.numeric_value == 10

    def test_all_moods_have_values(self):
        for mood in MoodState:
            assert isinstance(mood.numeric_value, int)
            assert 1 <= mood.numeric_value <= 10


class TestTechnique:
    def test_create_technique(self):
        tech = Technique(
            name="Test Technique",
            style=MeditationStyle.BREATH_AWARENESS,
            description="A test technique",
            instructions=["Step 1", "Step 2"],
            benefits=["Benefit 1"],
        )
        assert tech.name == "Test Technique"
        assert len(tech.instructions) == 2


class TestGuidedScript:
    def test_full_script(self):
        script = GuidedScript(
            id="test_01",
            title="Test Script",
            style=MeditationStyle.BREATH_AWARENESS,
            duration_minutes=10,
            introduction="Welcome.",
            body_segments=["Part 1.", "Part 2."],
            closing="Goodbye.",
        )
        full = script.full_script
        assert "Welcome." in full
        assert "Part 1." in full
        assert "Goodbye." in full

    def test_segment_count(self):
        script = GuidedScript(
            id="test_02",
            title="Test",
            style=MeditationStyle.BODY_SCAN,
            duration_minutes=15,
            introduction="Hello",
            body_segments=["A", "B", "C"],
            closing="End",
        )
        assert script.segment_count == 3


class TestMilestone:
    def test_create_milestone(self):
        m = Milestone(
            name="Test Badge",
            description="A test milestone",
            milestone_type=MilestoneType.SESSION_COUNT,
            threshold=10,
        )
        assert not m.achieved
        assert m.achieved_at is None
