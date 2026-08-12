import datetime as dt

import pytest

import final_project.pneumovac as pneumovac


@pytest.fixture
def age():
    return 30


@pytest.fixture
def keys():
    return [1]


def test_calculate_age(monkeypatch):
    class FixedDate:
        @classmethod
        def today(cls):
            return dt.date(2026, 8, 11)

    monkeypatch.setattr(pneumovac, "date", FixedDate)

    assert pneumovac.calculate_age(dt.date(2026, 8, 11)) == 0
    assert pneumovac.calculate_age(dt.date(2000, 11, 21)) == 25
    assert pneumovac.calculate_age(dt.date(1990, 3, 15)) == 36
    assert pneumovac.calculate_age(dt.date(1950, 12, 15)) == 75


def test_eligibility_by_age(age):
    assert pneumovac.eligibility(65, []) is True
    assert pneumovac.eligibility(70, []) is True


def test_eligibility_by_condition_key(age, keys):
    assert pneumovac.eligibility(30, [1]) is True
    assert pneumovac.eligibility(30, [99]) is False
    assert pneumovac.eligibility(30, []) is False



if __name__ == "__main__":
    import pytest
    pytest.main([__file__])