class SimpleClass():
    counter = 0
    
    def __init__(self):
        # self.__class__.counter += 1
        self.count()

    @classmethod
    def count(cls):
        cls.counter += 1


if __name__ == "__main__":
    lista = [SimpleClass(), SimpleClass()]
    print(SimpleClass.counter)  # Esperado 2
