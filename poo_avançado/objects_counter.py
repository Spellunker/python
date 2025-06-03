class SimpleClass():
    _counter = 0
    
    def __init__(self):
        SimpleClass._counter += 1


if __name__ == "__main__":
    lista = [SimpleClass(), SimpleClass()]
    print(SimpleClass._counter)  # Esperado 2
