#!/usr/bin/python3
# -*- coding: utf-8 -*-

with open("persons.csv") as file:
    for register in file:
        print("Name: {}, Age: {}".format(*register.strip().split(",")))

if file.closed:
    print("File already closed")
