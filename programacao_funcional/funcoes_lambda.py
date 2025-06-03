sales = (
    {"quantity": 2, "price": 10},
    {"quantity": 3, "price": 20},
    {"quantity": 5, "price": 14}
)

totals = tuple(
    map(
        lambda sale: sale["quantity"] * sale["price"],
        sales
    )
)

print("Prices:", list(totals))
print("Total price:", sum(totals))
