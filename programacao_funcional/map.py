list_1 = [1, 2, 3]
double = map(lambda x: x * 2, list_1)
print(list(double))


list_2 = [
    {"name": "John", "age": 31},
    {"name": "Mary", "age": 37},
    {"name": "Joseph", "age": 26},
]
just_names = map(lambda n: n["name"], list_2)
print(list(just_names))

just_ages = map(lambda n: n["age"], list_2)
print(sum(just_ages))

# challenge: using map return phrase "<name> has <age> years"
names = map(lambda n: n["name"], list_2)
ages = map(lambda n: n["age"], list_2)
for name, age in zip(names, ages):
    print(f"{name} has {age} years")

phrases = map(lambda p: f"{p['name']} has {p['age']} years", list_2)
print(list(phrases))

phrases = map(lambda p: f"{p['name']} has {p['age']} years", list_2)
for phrase in phrases:
    print(str(phrase))
