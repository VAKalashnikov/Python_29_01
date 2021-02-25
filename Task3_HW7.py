class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - other.number

    def __truediv__(self, other):
        return self.number // other.number

    def __mul__(self, other):
        return self.number * other.number

    def make_order(self, row):
        result = ''
        for i in range(int(self.number / row)):
            result += '*' * row + '\n'
        result += '*' * (self.number % row) + '\n'
        return result


cell_1 = Cell(9)
cell_2 = Cell(3)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 / cell_2)
print(cell_1 * cell_2)
print(cell_1.make_order(7))
