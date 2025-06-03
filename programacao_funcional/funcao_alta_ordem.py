from funcao_primeira_classe import double, square


def process(title, lista, function):
    print(f"Processing: {title}")
    for i in lista:
        print(i, "=>", function(i))


if __name__ == "__main__":
    process("Double from 1 to 10", range(1, 11), double)
    process("Square from 1 to 10", range(1, 11), square)
