def rainbow_colors():
    yield "red"  # retorno parcial
    yield "orange"
    yield "yellow"
    yield "green"
    yield "blue"
    yield "indigo"
    yield "violet"


if __name__ == "__main__":
    generator = rainbow_colors()
    print(type(generator))
    while True:
        print(next(generator))
