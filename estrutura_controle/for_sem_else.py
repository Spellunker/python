#!/usr/bin/python3
# -*- coding: utf-8 -*-

FORBIDDEN_WORDS = ("soccer", "religion", "politics")
texts = [
    "João likes soccer and politics",
    "The beach was fun"
]

for text in texts:
    found = False
    for word in text.lower().split():
        if word in FORBIDDEN_WORDS:
            print("There are at least one forbidden word in the text: ", word)
            found = True
            break

if not found:
    print("Text authorized: ", text)