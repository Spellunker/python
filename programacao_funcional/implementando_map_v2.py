# Simplified map implemention
def to_map(function, lista):
    return (function(number) for number in lista)


if __name__ == "__main__":
    print(tuple(to_map(lambda x: x ** 2, [2, 3, 4])))
