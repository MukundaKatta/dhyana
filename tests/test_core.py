"""Tests for Dhyana."""
from src.core import Dhyana
def test_init(): assert Dhyana().get_stats()["ops"] == 0
def test_op(): c = Dhyana(); c.process(x=1); assert c.get_stats()["ops"] == 1
def test_multi(): c = Dhyana(); [c.process() for _ in range(5)]; assert c.get_stats()["ops"] == 5
def test_reset(): c = Dhyana(); c.process(); c.reset(); assert c.get_stats()["ops"] == 0
def test_service_name(): c = Dhyana(); r = c.process(); assert r["service"] == "dhyana"
