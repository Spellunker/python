#!/usr/bin/python3
# -*- coding: utf-8 -*-


def age_group(value):
    age = int(value)

    if 0 <= age <= 18:
        return "underage"
    elif age in range(18, 65):
        return "adult"
    elif age in range(65, 100):
        return "senior"
    elif age >= 100:
        return "sage"
    else:
        return "invalid age"


if __name__ == "__main__":
    ages = (17, 0, 35, 87, 113, -2)
    for age in ages:  # for age in (17, 0, 35, 87, 113, -2)
        print(f"{age}: {age_group(age)}")
