from functools import reduce

people = [
    {"name": "Peter", "age": 11},
    {"name": "Mariana", "age": 18},
    {"name": "Arthur", "age": 26},
    {"name": "Rebeca", "age": 6},
    {"name": "James", "age": 19},
    {"name": "Gabriela", "age": 17},
]

ages_sum = reduce(lambda ages, p: ages + p["age"], people, 0)
print(ages_sum)

just_ages = map(lambda n: n["age"], people)
underages = filter(lambda age: age < 18, just_ages)
underages_sum = reduce(lambda underage_ages, p: underage_ages + p,
                       underages, 0)
print(underages_sum)
