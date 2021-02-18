class Road:

    def __init__(self, length, width):
        self.length = length
        self.width = width
        self.weight = 25
        self.thickness = 0.05

    def mass(self):
        mass = self.length * self.width * self.weight * self.thickness
        print("Нужно примерно {} кг асфальта ".format(round(mass)))


mkad = Road(108.9 * 1000, 30)
mkad.mass()
