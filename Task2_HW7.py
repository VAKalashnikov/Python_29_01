from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    @abstractmethod
    def info(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption


class Coat(Clothes):

    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5

    def info(self):
        return "{} ткани нужно примерно для данного пальто.".format(round(self.param / 6.5) + 0.5)


class Suit(Clothes):
    @property
    def consumption(self):
        return (2 * self.param + 0.3) / 100

    def info(self):
        return "{} ткани нужно примерно для данного костюма.".format(round(2 * self.param + 0.3) / 100)



coat = Coat(52)
suit = Suit(180)

print(coat.info())
print(suit.info())

print(coat + suit, "понадобится всего ткани.")
