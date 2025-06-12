from calendar import mdays, month_name
from functools import reduce


# List all months with 31 days
def month_with_31(month): return mdays[month] == 31


def get_month_name(month): return month_name[month]


def join_months(all, month_name): return f"{all}\n- {month_name}"


if __name__ == "__main__":
    print(reduce(join_months,
                 map(get_month_name,
                     filter(month_with_31, range(1, 13))
                     ), "Months with 31 days:"
                 )
          )
