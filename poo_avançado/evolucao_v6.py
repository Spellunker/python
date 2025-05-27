from abc import ABCMeta, abstractproperty


class Human(metaclass=ABCMeta):
    # class atribute
    specie = "Homo Sapiens"

    def __init__(self, name):
        self.name = name
        self._age = None

    @abstractproperty
    def inteligent(self):
        pass

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age must be a positive number")
        self._age = age

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

    @property
    def inteligent(self):
        return False


class HomoSapiens(Human):
    specie = Human.species()[-1]

    @property
    def inteligent(self):
        return True


if __name__ == "__main__":

    """    try:
        anonym = Human("John Doe")
        print(anonym.inteligent)
    except TypeError:
        print("Abstract class")"""

    joseph = HomoSapiens("Joseph")
    print("{} of the {} class, inteligent: {}"
          .format(joseph.name, joseph.__class__.__name__, joseph.inteligent))

    grogn = Neanderthal("Grogn")
    print("{} of the {} class, inteligent: {}"
          .format(grogn.name, grogn.__class__.__name__, grogn.inteligent))
