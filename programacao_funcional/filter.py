people = [
    {"name": "Peter", "age": 11},
    {"name": "Mariana", "age": 18},
    {"name": "Arthur", "age": 26},
    {"name": "Rebeca", "age": 6},
    {"name": "James", "age": 19},
    {"name": "Gabriela", "age": 17},
]

underages = filter(lambda p: p["age"] < 18, people)
print(list(underages))

# challenge name > 6 characters
name_len = filter(lambda n: len(n["name"]) >= 7, people)
print(tuple(name_len))
