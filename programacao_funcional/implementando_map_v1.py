# Simplified map implemention
def to_map(function, lista):
    for number in lista:
        yield function(number)


if __name__ == "__main__":
    print(list(to_map(lambda x: x ** 2, [2, 3, 4])))
