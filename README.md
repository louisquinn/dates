# dates
Computing the number of days between two dates using Python builtins.

# Installation

* A Python VM is recommended:

```shell
virtualenv --system-site-packages dates-env

source dates-env/bin/activate
pip install --upgrade pip
```

* Install with pip:

```shell
pip install .
```

# Usage

After pip installing the `dates` module, a `dates` binary will be available. Else, you can run the main script.

The script takes two positional date arguments in the format: `YYYY-MM-DD`. Exceptions will be raised if the dates
do not follow this format.

Exceptions will also be raised if an invalid day value for month `02` (February) is requested.

* With binary:

```shell
dates 2012-01-01 2012-01-10

# prints: "The number of days between: '2012-01-01' and '2012-01-10' is 8 days."
```

* With python script:

```shell
python dates/main.py 2021-12-01 2017-12-14

# prints: The number of days between: '2021-12-01' and '2017-12-14' is 1447 days.
```

Some invalid requests:

```shell
# Raises:
# AssertionError: Invalid date format: 01-01-2020. Expected: 'YYYY-MM-DD'.
dates 01-01-2020 2020-01-01

# Raises:
# AssertionError: Invalid date format: 20000-01-01. Expected: 'YYYY-MM-DD'.
dates 20000-01-01 2020-01-01

# Raises:
# ValueError: Invalid day '29' for month: '2'.
# dates.date.ValidDayInMonthException: Invalid day: '29' for month: '2'. The maximum days is '28'. The year '2022' is not a leap year.
dates 2022-02-29 2020-01-01
```

# Tests

From the `dates` repository root directory, run `pytest`. Note: requires the `pytest` package to be installed

* Install `pytests`:

```shell
pip install --upgrade pytests
```

* Run tests:

```shell
pytest
```

# Contributing

Please ensure `pre-commit` installed and initialized:

```shell
pip install --upgrade pre-commit

pre-commit install
```
