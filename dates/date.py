import re
from typing import Tuple

from dates.utils import (
    DAYS_IN_MONTH,
    LEAP_YR_MONTH,
    days_in_month,
    is_leap_year,
    num_days_before_month,
    num_days_before_year,
)


class ValidYearException(Exception):
    """
    Exception for invalid year.
    """

    def __init__(self, month: int):
        message = f"Invalid year: '{month}'. Must be a value greater than 0000."
        super(ValidYearException, self).__init__(message)


class ValidMonthException(Exception):
    """
    Exception for invalid month.
    """

    def __init__(self, month: int):
        message = f"Invalid month: '{month}'. Must be a value 1 <= month <= 12."
        super(ValidMonthException, self).__init__(message)


class ValidDayInMonthException(Exception):
    """
    Exception for invalid day int for a particular month and year.
    """

    def __init__(self, year: int, month: int, day: int, valid_days: int, leap_year: bool):
        leap_month = month == LEAP_YR_MONTH

        message = f"Invalid day: '{day}' for month: '{month}'. The maximum days is '{valid_days}'."

        feb_leap_year_days = DAYS_IN_MONTH[LEAP_YR_MONTH] + 1
        if leap_month and leap_year and day > feb_leap_year_days:
            message = (
                f"{message} '{year}' is a leap year, therefore {month} "
                f"can only have a maximum of {feb_leap_year_days} days."
            )

        if leap_month and not leap_year:
            message = f"{message} The year '{year}' is not a leap year."

        super(ValidDayInMonthException, self).__init__(message)


class Date:
    """
    Date module. Stores a date's year, month and day and can compute the absolute number of days between
    two Date modules.
    """

    VALID_DATE_PATTERN = r"^(\d{4})-(\d{2})-(\d{2})$"

    def __init__(self, date: str):
        """
        Initializes a Date module with a date string.

        :param date: A date string in the format: 'YYYY-MM-DD'.
        """
        self.date = date

        self.year, self.month, self.day = self._compile()

        # Assertions here.
        self._assert_validity()

    def _compile(self) -> Tuple[int, int, int]:
        """
        Compile a date string into year, month and day integers.

        :return: Tuple of ints representing (year, month, day)
        """
        pattern = re.compile(self.VALID_DATE_PATTERN)
        result = pattern.match(self.date)

        assert result is not None, f"Invalid date format: {self.date}. Expected: 'YYYY-MM-DD'."

        year = int(result.group(1))
        month = int(result.group(2))
        day = int(result.group(3))

        return year, month, day

    def _assert_validity(self):
        try:
            self._assert_valid_year()
            self._assert_valid_month()
            self._assert_valid_day_in_month()

        except ValidMonthException as e:
            raise ValueError(f"Invalid month '{self.month}'.") from e

        except ValidDayInMonthException as e:
            raise ValueError(f"Invalid day '{self.day}' for month: '{self.month}'.") from e

    def _assert_valid_year(self) -> None:
        if self.year <= 0:
            raise ValidYearException(self.year)

    def _assert_valid_month(self) -> None:
        if not 1 <= self.month <= 12:
            raise ValidMonthException(self.month)

    def _assert_valid_day_in_month(self) -> None:
        leap_year = is_leap_year(self.year)

        valid_days = days_in_month(self.year, self.month)

        if not 1 <= self.day <= valid_days:
            raise ValidDayInMonthException(self.year, self.month, self.day, valid_days=valid_days, leap_year=leap_year)

    def diff_from_time_origin_as_days(self) -> int:
        """
        Difference from "time origin", considering 0001-01-01 as day 1.

        :return: Number of days.
        """
        days_before_year = num_days_before_year(self.year)
        days_before_month = num_days_before_month(self.year, self.month)

        return days_before_year + days_before_month + self.day

    def __sub__(self, other: "Date") -> int:
        """
        Computes the absolute number of days between two Date objects.

        :param other: The other Date object.
        :return: Absolute number of days between Date objects.
        """
        ord_1 = self.diff_from_time_origin_as_days()
        ord_2 = other.diff_from_time_origin_as_days()

        return abs(ord_1 - ord_2) - 1

    def __str__(self):
        return f"{self.year}-{str(self.month).zfill(2)}-{str(self.day).zfill(2)}"
