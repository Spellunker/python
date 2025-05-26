class Human:
    #class atribute
    specie = "Homo Sapiens"

    def __init__(self, name):
        self.name = name

    def from_caves(self):
        self.specie = "Homo Neanderthalensis"
        return self


if __name__ == "__main__":
    joseph = Human("Joseph")
    grokn = Human("Grokn").from_caves()

    print(f"Human.specie: {Human.specie}")
    print(f"Joseph.specie: {joseph.specie}")
    print(f"Grokn.specie: {grokn.specie}")
