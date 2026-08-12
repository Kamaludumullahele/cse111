import datetime as dt
import final_project.pneumovacc as pneumovacc



def test_calculate_age(monkeypatch):
    class FixedDate:
        @classmethod
        def today(cls):
            return dt.date(2026, 8, 11)

    monkeypatch.setattr(pneumovacc, "date", FixedDate)

    assert pneumovacc.calculate_age(dt.date(2026, 8, 11)) == 0
    assert pneumovacc.calculate_age(dt.date(2000, 11, 21)) == 25
    assert pneumovacc.calculate_age(dt.date(1990, 3, 15)) == 36
    assert pneumovacc.calculate_age(dt.date(1950, 12, 15)) == 75


def test_eligibility_by_age(age):
    assert pneumovacc.eligibility(65, []) is True
    assert pneumovacc.eligibility(70, []) is True


def test_eligibility_by_condition_key(age, keys):
    assert pneumovacc.eligibility(30, [1]) is True
    assert pneumovacc.eligibility(30, [99]) is False
    assert pneumovacc.eligibility(30, []) is False



if __name__ == "__main__":
    import pytest
    pytest.main([__file__])