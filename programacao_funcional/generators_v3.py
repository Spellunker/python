def sequence():
    number = 0
    while True:
        number += 1
        yield number


if __name__ == "__main__":
    seq = sequence()

    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
    print(next(seq))
