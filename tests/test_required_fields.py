import pytest

from src.required_fields import require_required_field


def test_rejects_none():
    with pytest.raises(ValueError):
        require_required_field(None, "name")


def test_rejects_blank_string():
    with pytest.raises(ValueError):
        require_required_field("   ", "name")


def test_returns_trimmed_string():
    assert require_required_field("  alice  ", "name") == "alice"
