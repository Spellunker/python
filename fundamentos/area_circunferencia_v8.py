#!/usr/bin/python3
from math import pi


def circle(radius):
    print("Circle area", pi * float(radius) ** 2)


if __name__ == "__main__":
    radius = input("Input the radius")
    circle(radius)
