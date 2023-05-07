import pytest

from dates import Date, ValidDayInMonthException
from dates.utils import DAYS_IN_MONTH


def test_month_is_not_zero():
    with pytest.raises(Exception):
        Date("2012-00-30")


def test_day_is_not_zero():
    with pytest.raises(Exception):
        Date("2012-01-00")


def test_year_is_not_zero():
    with pytest.raises(Exception):
        Date("0000-01-01")


def test_max_day_for_months():
    def test(year: int):
        strings = [
            f"{year}-{str(i).zfill(2)}-{str(days).zfill(2)}" for i, days in enumerate(DAYS_IN_MONTH[1:], start=1)
        ]

        try:
            [Date(s) for s in strings]
        except ValidDayInMonthException:
            assert False

        assert True

    test(2012)  # Leap year.
    test(2013)  # Normal year.
