#!/usr/bin/python3
def execute(function):
    if callable(function):
        function()


def good_morning():
    print("Good monrning!")


def good_afternoon():
    print("Good afternoon!")


if __name__ == "__main__":
    execute(good_morning)
    execute(good_afternoon)
    execute(1)
