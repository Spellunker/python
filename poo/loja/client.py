from .person import Person


def get_date(sale):
    return sale.date


class Client(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.sales = []

    def register_sale(self, sale):
        self.sales.append(sale)

    def get_last_sale_date(self):
        return None if not self.sales else \
            sorted(self.sales, key=get_date)[-1].date

    def sales_total(self):
        total = 0
        for sale in self.sales:
            total += sale.value
        return total
