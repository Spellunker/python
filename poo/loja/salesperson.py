from .person import Person


class Salesperson(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
