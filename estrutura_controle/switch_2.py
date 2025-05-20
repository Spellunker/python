#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""def get_weekday(day):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }
    return days.get(day, "#INVALID#")


weekend = ("Sunday", "Saturday")

if __name__ == "__main__":
    for day in range(8):
        compare = get_weekday(day)
        print(f"{day}: {compare}")
        if compare in weekend:
            print("This day is in the weekend")
        else:
            print("This day isn`t in the weekend")"""


def get_day_type(day):
    days = {
        1: "Weekend",
        2: "Weekday",
        3: "Weekday",
        4: "Weekday",
        5: "Weekday",
        6: "Weekday",
        7: "Weekend",
    }
    return days.get(day, "#INVALID#")


if __name__ == "__main__":
    for day in range(9):
        print(f"{day}: {get_day_type(day)}")
