#!/usr/bin/python3
def final_price_calc(gross_price, tax_calc, **params):
    return gross_price + gross_price * tax_calc(**params)


def x_tax(imported):
    return 0.22 if imported else 0.13


def y_tax(explosive, mult_factor=1):
    return 0.11 * mult_factor if explosive else 0


if __name__ == "__main__":
    gross_price = 134.98
    final_price = final_price_calc(gross_price, x_tax, imported=True)
    final_price = final_price_calc(final_price, y_tax,
                                   explosive=True, mult_factor=1.5)
    print(f"Final price R${final_price}")
