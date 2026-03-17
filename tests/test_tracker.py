"""Tests for tracker module."""

from datetime import date

from dhyana.tracker.sessions import SessionTracker
from dhyana.tracker.stats import MeditationStats
from dhyana.tracker.progress import ProgressTracker
from dhyana.models import MeditationStyle, MoodState, MilestoneType


class TestSessionTracker:
    def test_log_session(self):
        st = SessionTracker()
        session = st.log_session(
            technique=MeditationStyle.BREATH_AWARENESS,
            duration_minutes=15,
        )
        assert session.technique == MeditationStyle.BREATH_AWARENESS
        assert st.total_sessions() == 1

    def test_log_session_with_mood(self):
        st = SessionTracker()
        session = st.log_session(
            technique=MeditationStyle.METTA,
            duration_minutes=20,
            mood_before=MoodState.STRESSED,
            mood_after=MoodState.CALM,
        )
        assert session.mood_improvement is not None
        assert session.mood_improvement > 0

    def test_total_minutes(self):
        st = SessionTracker()
        st.log_session(MeditationStyle.BREATH_AWARENESS, 10)
        st.log_session(MeditationStyle.ZAZEN, 20)
        assert st.total_minutes() == 30

    def test_average_duration(self):
        st = SessionTracker()
        st.log_session(MeditationStyle.BREATH_AWARENESS, 10)
        st.log_session(MeditationStyle.ZAZEN, 20)
        assert st.average_duration() == 15.0

    def test_technique_frequency(self):
        st = SessionTracker()
        st.log_session(MeditationStyle.BREATH_AWARENESS, 10)
        st.log_session(MeditationStyle.BREATH_AWARENESS, 15)
        st.log_session(MeditationStyle.ZAZEN, 20)
        freq = st.technique_frequency()
        assert freq[MeditationStyle.BREATH_AWARENESS] == 2
        assert freq[MeditationStyle.ZAZEN] == 1

    def test_favorite_technique(self):
        st = SessionTracker()
        st.log_session(MeditationStyle.VIPASSANA, 20)
        st.log_session(MeditationStyle.VIPASSANA, 20)
        st.log_session(MeditationStyle.METTA, 15)
        assert st.favorite_technique() == MeditationStyle.VIPASSANA

    def test_get_sessions_by_date(self):
        st = SessionTracker()
        st.log_session(MeditationStyle.BREATH_AWARENESS, 10)
        sessions = st.get_sessions_by_date(date.today())
        assert len(sessions) == 1

    def test_delete_session(self):
        st = SessionTracker()
        session = st.log_session(MeditationStyle.BREATH_AWARENESS, 10)
        assert st.delete_session(session.id)
        assert st.total_sessions() == 0

    def test_empty_tracker(self):
        st = SessionTracker()
        assert st.total_sessions() == 0
        assert st.total_minutes() == 0
        assert st.average_duration() == 0.0
        assert st.favorite_technique() is None

    def test_average_mood_improvement(self):
        st = SessionTracker()
        st.log_session(
            MeditationStyle.BREATH_AWARENESS, 10,
            mood_before=MoodState.STRESSED,
            mood_after=MoodState.CALM,
        )
        st.log_session(
            MeditationStyle.METTA, 15,
            mood_before=MoodState.NEUTRAL,
            mood_after=MoodState.PEACEFUL,
        )
        avg = st.average_mood_improvement()
        assert avg is not None
        assert avg > 0


class TestMeditationStats:
    def test_total_time(self):
        st = SessionTracker()
        st.log_session(MeditationStyle.BREATH_AWARENESS, 30)
        st.log_session(MeditationStyle.ZAZEN, 30)
        ms = MeditationStats(st)
        assert ms.total_time_minutes() == 60
        assert ms.total_time_hours() == 1.0

    def test_consistency_score(self):
        st = SessionTracker()
        st.log_session(MeditationStyle.BREATH_AWARENESS, 10)
        ms = MeditationStats(st)
        score = ms.consistency_score(30)
        # At least today was practiced
        assert score > 0
        assert score <= 1.0

    def test_unique_techniques(self):
        st = SessionTracker()
        st.log_session(MeditationStyle.BREATH_AWARENESS, 10)
        st.log_session(MeditationStyle.ZAZEN, 20)
        st.log_session(MeditationStyle.BREATH_AWARENESS, 15)
        ms = MeditationStats(st)
        assert ms.unique_techniques_used() == 2

    def test_technique_distribution(self):
        st = SessionTracker()
        st.log_session(MeditationStyle.BREATH_AWARENESS, 10)
        st.log_session(MeditationStyle.BREATH_AWARENESS, 10)
        st.log_session(MeditationStyle.ZAZEN, 10)
        st.log_session(MeditationStyle.ZAZEN, 10)
        ms = MeditationStats(st)
        dist = ms.technique_distribution()
        assert dist[MeditationStyle.BREATH_AWARENESS] == 50.0
        assert dist[MeditationStyle.ZAZEN] == 50.0

    def test_empty_stats(self):
        ms = MeditationStats()
        assert ms.total_sessions() == 0
        assert ms.current_streak() == 0
        assert ms.longest_streak() == 0

    def test_weekly_summary(self):
        st = SessionTracker()
        st.log_session(MeditationStyle.BREATH_AWARENESS, 15)
        ms = MeditationStats(st)
        summary = ms.weekly_summary()
        assert summary["sessions"] >= 1
        assert summary["total_minutes"] >= 15

    def test_mood_improvement_stats_empty(self):
        ms = MeditationStats()
        stats = ms.mood_improvement_stats()
        assert stats["average"] is None


class TestProgressTracker:
    def test_check_first_session_milestone(self):
        st = SessionTracker()
        st.log_session(MeditationStyle.BREATH_AWARENESS, 10)
        ms = MeditationStats(st)
        pt = ProgressTracker(st, ms)
        newly = pt.check_milestones()
        names = [m.name for m in newly]
        assert "Beginner Mind" in names
        assert "First Step" in names

    def test_achieved_milestones(self):
        st = SessionTracker()
        st.log_session(MeditationStyle.BREATH_AWARENESS, 10)
        ms = MeditationStats(st)
        pt = ProgressTracker(st, ms)
        pt.check_milestones()
        achieved = pt.achieved_milestones
        assert len(achieved) > 0

    def test_pending_milestones(self):
        pt = ProgressTracker()
        pending = pt.pending_milestones
        assert len(pending) > 0

    def test_progress_summary(self):
        st = SessionTracker()
        st.log_session(MeditationStyle.BREATH_AWARENESS, 10)
        ms = MeditationStats(st)
        pt = ProgressTracker(st, ms)
        summary = pt.progress_summary()
        assert "total_sessions" in summary
        assert "current_streak" in summary
        assert "milestones_achieved" in summary

    def test_next_milestone(self):
        pt = ProgressTracker()
        nxt = pt.next_milestone()
        assert nxt is not None

    def test_milestone_progress(self):
        st = SessionTracker()
        st.log_session(MeditationStyle.BREATH_AWARENESS, 10)
        ms = MeditationStats(st)
        pt = ProgressTracker(st, ms)
        for m in pt.milestones:
            prog = pt.get_milestone_progress(m)
            assert 0.0 <= prog <= 100.0

    def test_explorer_milestone(self):
        st = SessionTracker()
        st.log_session(MeditationStyle.BREATH_AWARENESS, 10)
        st.log_session(MeditationStyle.ZAZEN, 10)
        st.log_session(MeditationStyle.METTA, 10)
        ms = MeditationStats(st)
        pt = ProgressTracker(st, ms)
        newly = pt.check_milestones()
        names = [m.name for m in newly]
        assert "Explorer" in names
