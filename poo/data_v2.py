class Data:
    def __init__(self, day=1, month=1, year=1970):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"


d1 = Data(5, 12, 2019)
"""d1.day = 5
d1.month = 12
d1.year = 2019"""
print(d1)

d2 = Data(year=2022, month=12)
d2.day = 12
"""d2.month = 11
d2.year = 2020"""
print(d2)
