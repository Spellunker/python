#!/usr/bin/python3
# -*- coding: utf-8 -*-

word = "paving stone"
for letter in word:
    print(letter, end=", ")
print("End")

approved = ["Rafaela", "Pedro", "Renato", "Maria"]
for name in approved:
    print(name)

for position, name in enumerate(approved):
    print(f"{position + 1})", name)

weekdays = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
for day in weekdays:
    print(f"Today is {day}")

for number in {1, 2, 3, 4, 5, 6}:
    print(number)
