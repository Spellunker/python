def multiply(x):
    def calc(y):
        return x * y
    return calc


if __name__ == "__main__":
    double = multiply(2)
    triple = multiply(3)
    print(double)
    print(triple)
    print(f"Triple of 3 is {triple(3)}")
    print(f"Double of 7 is {double(7)}")
