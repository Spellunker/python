class Human:
    # class atribute
    specie = "Homo Sapiens"

    def __init__(self, name):
        self.name = name

    def from_caves(self):
        self.specie = "Homo Neanderthalensis"
        return self

    @staticmethod
    def species():
        adjectives = ("Habilis", "Erectus", "Neanderthalensis", "Sapiens")
        return ("Australopiteco",) + tuple(f"Homo {adj}" for adj in adjectives)

    @classmethod
    def is_evolved(cls):
        return cls.specie == cls.species()[-1]


class Neanderthal(Human):
    specie = Human.species()[-2]


class HomoSapiens(Human):
    specie = Human.species()[-1]


if __name__ == "__main__":
    joseph = HomoSapiens("Joseph")
    grokn = Neanderthal("Grokn")
    print(f"Evolved (from class): {','.join(HomoSapiens.species())}")
    print(f"Evolved (from instance): {','.join(joseph.species())}")
    print(f"Is Homo Sapiens evolved? {HomoSapiens.is_evolved()}")
    print(f"Is Neanderthal evolved? {Neanderthal.is_evolved()}")
    print(f"Is Joseph evolved? {joseph.is_evolved()}")
    print(f"Is Grokn evolved? {grokn.is_evolved()}")
