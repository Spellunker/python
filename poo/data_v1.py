class Data:
    def __str__(self):
        return f"{self.day}/{self.month}/{self.year}"


d1 = Data()
d1.day = 5
d1.month = 12
d1.year = 2019
print(d1)

d2 = Data()
d2.day = 7
d2.month = 11
d2.year = 2020
print(d2)
