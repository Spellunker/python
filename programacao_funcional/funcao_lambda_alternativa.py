sales = (
    {"quantity": 2, "price": 10},
    {"quantity": 3, "price": 20},
    {"quantity": 5, "price": 14}
)


def calc_total_price(sale):
    return sale["quantity"] * sale["price"]


totals = tuple(map(calc_total_price, sales))

print("Prices:", list(totals))
print("Total price:", sum(totals))
