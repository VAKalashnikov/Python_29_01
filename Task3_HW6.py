class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

sample_worker = Position("Владимир", "Калашников", "стажер", "30000", "10000")
print(sample_worker.get_full_name())
print(sample_worker.get_total_income())

print("Имя работника: {}".format(sample_worker.name))
print("Фамилия работника: {}".format(sample_worker.surname))
print("Должность работника: {}".format(sample_worker.position))
print("Зарплата работника: {}".format(sample_worker._income["wage"]))
print("Бонус работника: {}".format(sample_worker._income["bonus"]))