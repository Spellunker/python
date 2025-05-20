#!/usr/bin/python3
# -*- coding: utf-8 -*-

def get_weekday(day):
    days = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday",
    }
    return days.get(day, "** invalid **")


if __name__ == "__main__":
    for day in range (0,9):
        print(f"{day}: {get_weekday(day)}")
