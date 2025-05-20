def calc_final_price(gross_price, tax_calc, *params):
    return gross_price + gross_price * tax_calc(*params)


def x_tax(imported):
    return 0.22 if imported else 0.13


def y_tax(explosive, mult_factor = 1.0):
    return 0.11 * mult_factor if explosive else 0


if __name__ == "__main__":
    gross_price = 134.98
    end_price = calc_final_price(gross_price, x_tax, True)
    end_price = calc_final_price(end_price, y_tax, True, 1.5)
    print(f"En price R${end_price}")
