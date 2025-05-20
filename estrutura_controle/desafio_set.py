#!/usr/bin/python3
# -*- coding: utf-8 -*-

FORBIDDEN_WORDS = {"soccer", "religion", "politics"}
texts = [
    "João likes soccer and politics",
    "The beach was fun"
]

for text in texts:
    intersect = FORBIDDEN_WORDS.intersection(set(text.lower().split()))
    if intersect:
        print(f"There is forbidden words in the text: {intersect}")
    else:
        print("Authorized text: ", text)
