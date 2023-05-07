import argparse

from dates import Date


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("date1", type=str, help="The first date in the format: 'YYYY-MM-DD'.")
    parser.add_argument("date2", type=str, help="The second date in the format: 'YYYY-MM-DD'.")

    return parser.parse_args()


def main():
    args = parse_args()

    date1 = Date(args.date1)
    date2 = Date(args.date2)

    diff = date1 - date2

    print(f"The number of days between: '{str(date1)}' and '{str(date2)}' is {diff} days.")


if __name__ == "__main__":
    main()
