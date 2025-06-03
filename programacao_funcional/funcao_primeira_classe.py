def double(x):
    return x * 2


def square(x):
    return x ** 2


if __name__ == "__main__":
    d = double
    print(d(5))

    s = square
    print(s(5))

    # alternately return double or square the numbers between 1 and 10
    funcs = [double, square] * 5
    for func, number in zip(funcs, range(1, 11)):
        print(f"The {func.__name__} of {number} is {func(number)}")
