#!/usr/bin/python3
# -*- coding: utf-8 -*-


def grade_concept(value):
    grade = float(value)

    if grade > 10 or grade < 0:
        return "Invalid grade"
    elif grade > 9:
        return "A"
    elif grade > 8:
        return "A-"
    elif grade > 7:
        return "B"
    elif grade > 6:
        return "B-"
    elif grade > 5:
        return "C"
    elif grade > 4:
        return "C-"
    elif grade > 3:
        return "D"
    elif grade > 2:
        return "D-"
    elif grade > 1:
        return "E"
    else:
        return "E-"


if __name__ == "__main__":
    value = float(input("Please input the grade: "))
    print(grade_concept(value))
