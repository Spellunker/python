#!/usr/bin/python3
# -*- coding: utf-8 -*-

with open("persons.csv") as file:
    with open("persons.txt", "w") as output:
        for register in file:
            person = register.strip().split(",")
            print("Name: {}, Age: {}".format(*person), file=output)

if file.closed:
    print("File already closed!")

if output.closed:
    print("Output file already closed!")
