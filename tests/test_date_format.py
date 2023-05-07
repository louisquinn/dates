import pytest

from dates import Date


def test_exception_year_last():
    with pytest.raises(Exception):
        Date("01-01-2020")


def test_missing_year():
    with pytest.raises(Exception):
        Date("01-01")


def test_missing_month_or_day():
    with pytest.raises(Exception):
        Date("2020-01")


def test_year_format():
    with pytest.raises(Exception):
        Date("202-01-01")

    with pytest.raises(Exception):
        Date("20000-01-01")
