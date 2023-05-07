from copy import deepcopy

# As per the Gregorian calendar:
# https://en.wikipedia.org/wiki/Gregorian_calendar#:~:text=A%20year%20is%20divided%20into%20twelve
DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Pad index 0 to avoid subtracting 1 every time.

LEAP_YR_MONTH = 2  # Feb.


def is_leap_year(year: int) -> bool:
    """
    Leap year rule from here:
    https://en.wikipedia.org/wiki/Leap_year#:~:text=Gregorian%20calendar%5Bedit%5D

    A leap year is every 4 years, except for years that are divisible by 100 but not by 400.

    :param year: A year integer.
    :return: True if a leap year else False.
    """
    # return (year % 4 == 0 or year % 100 == 0) or (year % 400 == 0)
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year: int, month: int) -> int:
    if is_leap_year(year) and month == LEAP_YR_MONTH:
        return DAYS_IN_MONTH[LEAP_YR_MONTH] + 1

    return DAYS_IN_MONTH[month]


def num_days_before_year(year: int) -> int:
    """
    Compute number of days between Jan 1st 0001 and Jan 1st on supplied year.

    :param year: A year integer.
    :return: Number of days.
    """
    year_prev = year - 1

    days_per_year = 365
    num_leap_years = num_leap_years_before_year(year)

    return year_prev * days_per_year + num_leap_years


def num_leap_years_before_year(year: int) -> int:
    """
    Compute the number of leap years from year 1.

    A leap year is every 4 years, except for years that are divisible by 100 but not by 400.

    :param year: A year integer.
    :return: Num leap years
    """
    y = year - 1
    return y // 4 - y // 100 + y // 400


def num_days_before_month(year: int, month: int) -> int:
    """
    Number of days between Jan 1 and 1st day of the given month.
    Uses the year to compute if the year is a leap year.

    :param year: A year integer. Used to compute leap years.
    :param month: A month integer.
    :return: Num days.
    """
    days = deepcopy(DAYS_IN_MONTH)

    if is_leap_year(year):
        days[LEAP_YR_MONTH] += 1

    return sum(days[1:month])
