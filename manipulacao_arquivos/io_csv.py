#!/usr/bin/python3
# -*- coding: utf-8 -*-

import csv

with open("persons.csv") as input:
    for person in csv.reader(input):
        print("Name: {}, Age: {}".format(*person))
