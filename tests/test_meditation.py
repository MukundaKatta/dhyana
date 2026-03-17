"""Tests for meditation module."""

from dhyana.meditation.guided import GuidedMeditation
from dhyana.meditation.timer import MeditationTimer, BellConfig
from dhyana.meditation.techniques import TechniqueLibrary
from dhyana.models import MeditationStyle, Difficulty


class TestGuidedMeditation:
    def test_has_20_plus_scripts(self):
        gm = GuidedMeditation()
        assert gm.count >= 20

    def test_get_by_id(self):
        gm = GuidedMeditation()
        script = gm.get_by_id("breath_01")
        assert script is not None
        assert script.title == "Arriving in the Present Moment"

    def test_get_by_style(self):
        gm = GuidedMeditation()
        breath_scripts = gm.get_by_style(MeditationStyle.BREATH_AWARENESS)
        assert len(breath_scripts) >= 2

    def test_get_by_duration(self):
        gm = GuidedMeditation()
        short_scripts = gm.get_by_duration(10)
        assert len(short_scripts) > 0
        assert all(s.duration_minutes <= 10 for s in short_scripts)

    def test_get_random(self):
        gm = GuidedMeditation()
        script = gm.get_random()
        assert script is not None
        assert script.title

    def test_get_random_by_style(self):
        gm = GuidedMeditation()
        script = gm.get_random(MeditationStyle.BODY_SCAN)
        assert script.style == MeditationStyle.BODY_SCAN

    def test_get_for_mood_stressed(self):
        gm = GuidedMeditation()
        scripts = gm.get_for_mood("stressed")
        assert len(scripts) > 0

    def test_get_for_mood_sad(self):
        gm = GuidedMeditation()
        scripts = gm.get_for_mood("sad")
        assert len(scripts) > 0

    def test_search(self):
        gm = GuidedMeditation()
        results = gm.search("breath")
        assert len(results) > 0

    def test_styles_available(self):
        gm = GuidedMeditation()
        styles = gm.get_styles_available()
        assert MeditationStyle.BREATH_AWARENESS in styles
        assert MeditationStyle.BODY_SCAN in styles
        assert MeditationStyle.LOVING_KINDNESS in styles

    def test_full_script_content(self):
        gm = GuidedMeditation()
        script = gm.get_by_id("breath_01")
        assert script is not None
        full = script.full_script
        assert len(full) > 100


class TestTechniqueLibrary:
    def test_has_15_plus_techniques(self):
        lib = TechniqueLibrary()
        assert lib.count >= 15

    def test_get_by_style(self):
        lib = TechniqueLibrary()
        tech = lib.get_by_style(MeditationStyle.VIPASSANA)
        assert tech is not None
        assert "Vipassana" in tech.name

    def test_get_by_name(self):
        lib = TechniqueLibrary()
        tech = lib.get_by_name("zazen")
        assert tech is not None

    def test_get_by_difficulty(self):
        lib = TechniqueLibrary()
        beginner = lib.get_by_difficulty(Difficulty.BEGINNER)
        assert len(beginner) > 0
        assert all(t.difficulty == Difficulty.BEGINNER for t in beginner)

    def test_get_beginner_techniques(self):
        lib = TechniqueLibrary()
        beginner = lib.get_beginner_techniques()
        assert len(beginner) >= 5

    def test_get_for_duration(self):
        lib = TechniqueLibrary()
        short = lib.get_for_duration(10)
        assert len(short) > 0

    def test_search(self):
        lib = TechniqueLibrary()
        results = lib.search("concentration")
        assert len(results) > 0

    def test_get_recommended_stressed(self):
        lib = TechniqueLibrary()
        recs = lib.get_recommended("stressed")
        assert len(recs) > 0

    def test_get_recommended_calm(self):
        lib = TechniqueLibrary()
        recs = lib.get_recommended("calm")
        assert len(recs) > 0

    def test_all_have_instructions(self):
        lib = TechniqueLibrary()
        for tech in lib.techniques:
            assert len(tech.instructions) >= 3
            assert len(tech.benefits) >= 2

    def test_vipassana_details(self):
        lib = TechniqueLibrary()
        v = lib.get_by_style(MeditationStyle.VIPASSANA)
        assert v is not None
        assert v.difficulty == Difficulty.INTERMEDIATE
        assert "India" in v.origin

    def test_zazen_details(self):
        lib = TechniqueLibrary()
        z = lib.get_by_style(MeditationStyle.ZAZEN)
        assert z is not None
        assert "Zen" in z.name

    def test_yoga_nidra_details(self):
        lib = TechniqueLibrary()
        yn = lib.get_by_style(MeditationStyle.YOGA_NIDRA)
        assert yn is not None
        assert yn.difficulty == Difficulty.BEGINNER

    def test_trataka_details(self):
        lib = TechniqueLibrary()
        t = lib.get_by_style(MeditationStyle.TRATAKA)
        assert t is not None
        assert "candle" in t.description.lower() or "gazing" in t.description.lower()

    def test_metta_details(self):
        lib = TechniqueLibrary()
        m = lib.get_by_style(MeditationStyle.METTA)
        assert m is not None
        assert "loving" in m.name.lower() or "metta" in m.name.lower()


class TestMeditationTimer:
    def test_create_timer(self):
        t = MeditationTimer()
        assert not t.is_running

    def test_start_stop(self):
        t = MeditationTimer()
        t.set_duration(10)
        result = t.start()
        assert result["status"] == "started"
        assert t.is_running

        result = t.stop()
        assert result["status"] == "completed"
        assert not t.is_running

    def test_tick(self):
        t = MeditationTimer()
        t.set_duration(1)  # 1 minute
        t.start()
        t.tick(30)
        assert t.elapsed_seconds == 30
        assert t.remaining_seconds == 30

    def test_tick_completion(self):
        t = MeditationTimer()
        t.set_duration(1)
        t.start()
        result = t.tick(60)
        assert result == "session_complete"
        assert not t.is_running

    def test_interval_bell(self):
        config = BellConfig(interval_bells=1, interval_minutes=5)
        t = MeditationTimer(bell_config=config)
        t.set_duration(20)
        t.start()
        result = t.tick(300)  # 5 minutes
        assert result == "interval_bell"

    def test_progress(self):
        t = MeditationTimer()
        t.set_duration(10)
        t.start()
        t.tick(300)  # 5 minutes
        prog = t.get_progress()
        assert prog["percent_complete"] == 50.0

    def test_format_time(self):
        t = MeditationTimer()
        assert t.format_time(0) == "00:00"
        assert t.format_time(65) == "01:05"
        assert t.format_time(600) == "10:00"

    def test_ambient_descriptions(self):
        t = MeditationTimer()
        ambients = t.available_ambients()
        assert "forest" in ambients
        assert "mountain" in ambients
        assert "ocean" in ambients

        desc = t.get_ambient_description("forest")
        assert len(desc) > 50
        assert "forest" in desc.lower()

    def test_bell_config(self):
        config = BellConfig(start_bells=2, end_bells=2, interval_bells=1, interval_minutes=10)
        t = MeditationTimer(bell_config=config)
        assert t.bell_config.start_bells == 2
        assert t.bell_config.interval_minutes == 10
