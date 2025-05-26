from datetime import datetime


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, {self.age} years old"

    def is_adult(self):
        adult = True if self.age >= 18 else False
        return adult


class Client(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.sales = []
        self.total = 0
        self.value = 0

    def register_sale(self, value):
        self.value = value
        self.sales.append(value)
        self.last_sale_date = datetime.now()
        return self.last_sale_date

    def get_last_sale_date(self):
        return f"The last sale date is {self.last_sale_date}"

    def sales_total(self):
        for value in self.sales:
            self.total += value
        return self.total


class Salesperson(Person):
    def __init__(self, name, age, salary=1500):
        super().__init__(name, age)
        self.salary = salary


class Sales():
    def __init__(self, salesperson="", date="", value=0):
        self.salesperson = salesperson
        self.date = date
        self.value = value


def main():
    client = Client("Arnaldo Jr", 30)
    print(client)

    salesperson = Salesperson("Vendedor 1", 25, 2000)
    print(salesperson)

    sales = Sales("Vendedor 1", client.register_sale(value=300), client.value)
    sales = Sales("Vendedor 1", client.register_sale(value=500), client.value)
    sales = Sales("Vendedor 1", client.register_sale(value=200), client.value)
    
    print(client.get_last_sale_date())
    print(client.sales_total())


if __name__ == '__main__':
    main()
