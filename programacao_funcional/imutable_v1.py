from calendar import mdays, month_name
from functools import reduce


# List all months with 31 days
def print_months():
    months_31 = filter(lambda month: mdays[month] == 31, range(1, 13))
    months_names = map(lambda month: month_name[month], months_31)
    months_print = reduce(lambda months_texts, m: f"{months_texts}\n- {m}",
                          months_names, "Months with 31 days")
    print(months_print)


def improved_print_months():
    print(
        reduce(lambda months_texts, m: f"{months_texts}\n- {m}",
               map(lambda month: month_name[month],
                   filter(lambda month: mdays[month] == 31, range(1, 13))),
               "Months with 31 days")
    )


if __name__ == "__main__":
    print_months()
    improved_print_months()
