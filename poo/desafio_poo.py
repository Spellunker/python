from datetime import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, {self.age} years old"

    def is_adult(self):
        adult = "Adult" if self.age >= 18 else "Not Adult"
        return adult


class Client(Person):
    def __init__(self, name, age):
        super.__init__(name, age)
        self.sales = []

    def register_sale(self, sale):
        self.sales.append(sale)
        get_last_sale_sate(last_sale_sate = datime.now())

    def get_last_sale_date(self, date)
        self.last_sale_date = date
        return f"The last sale date is {date}"

    def sales_total(self):
        pass


class Salesperson(Person):
    def __init__(self, name, age):
        super.__init__(name, age)
        self.salary = 1500


class Sales:
    def __init__(self, salesperson, date, value):
        self.salesperson = ""
        self.date = ""
        self.value = 0


def main():
    pass


if __name__ == '__main__':
    main()