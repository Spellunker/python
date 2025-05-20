#!/usr/bin/python3
from math import pi
import sys


def circle(radius):
    return pi * float(radius) ** 2


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("It`s necessary to inform the circle radius")
        print(f"syntax: {sys.argv[0][2:]} <radius>")
    else:
        radius = sys.argv[1]
        area = circle(radius)
        print("Circle Area is", area)
