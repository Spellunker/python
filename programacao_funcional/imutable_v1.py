#!/usr/bin/python3
from calendar import mdays, month_name
from functools import reduce


# List all months with 31 days
def print_months():
    months_31 = filter(lambda month: mdays[month] == 31, range(1, 13))
    months_names = map(lambda month: month_name[month], months_31)
    months_print = reduce(lambda months_texts, m: f"- {m}", months_names, 0)
    print(list(months_print))


if __name__ == "__main__":
    print_months()
