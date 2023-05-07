from datetime import date
from itertools import combinations
from random import randint

from dates import Date
from dates.utils import DAYS_IN_MONTH, LEAP_YR_MONTH, is_leap_year


def test_basics():
    assert Date("2012-01-10") - Date("2012-01-11") == 0
    assert Date("2012-01-01") - Date("2012-01-10") == 8
    assert Date("1801-06-13") - Date("1801-11-11") == 150
    assert Date("2021-12-01") - Date("2017-12-14") == 1447


def test_against_datetime_module():
    """

    Generates random dates and computes the diff with the `datetime` module.
    Asserts if our program generates the same result.

    We subtract 1 from the datetime result as it does not compute the absolute value.

    :return: None
    """

    num_dates = 100

    years = [randint(1, 9999) for i in range(num_dates)]
    months = [randint(1, 12) for i in range(num_dates)]

    # Generate valid dates.
    days = [
        randint(1, DAYS_IN_MONTH[m] + 1 if is_leap_year(y) and m == LEAP_YR_MONTH else DAYS_IN_MONTH[m])
        for y, m in zip(years, months)
    ]

    dates = list(zip(years, months, days))
    date_strings = [f"{str(y).zfill(4)}-{str(m).zfill(2)}-{str(d).zfill(2)}" for y, m, d in dates]

    pairs = list(combinations(dates, 2))
    pairs_strings = list(combinations(date_strings, 2))

    datetime_results = [
        abs((date(date1[0], date1[1], date1[2]) - date(date2[0], date2[1], date2[2])).days) - 1
        for date1, date2 in pairs
    ]

    date_results = [Date(date1) - Date(date2) for date1, date2 in pairs_strings]

    assert all([x == y for x, y in zip(datetime_results, date_results)])
