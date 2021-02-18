class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"Auto {self.name} started moving."

    def stop(self):
        return f"Auto {self.name} stopped."

    def turn(self, direction):
        return f"Auto {self.name} turned in {direction} direction."

    def show_speed(self):
        return f"Auto {self.name} if riding {self.speed} kmph."


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return "You are riding to fast!"


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return "You are riding too fast!"
        if self.speed < 20:
            return "Please, accelerate. You are moving too slow!!!"


simply_car = Car(70, "red", "Zhiguli", False)  # создадим объект базового класса

print(simply_car.show_speed())  # работает
print(simply_car.turn("north"))  # ну все методы пробовать не будем

ford_focus = TownCar(80, "black", "Ford", False)  # создадим TownCar

print(ford_focus.show_speed())
print(ford_focus.turn("west"))  # успешно

traktor = WorkCar(15, "orange", "MTZ", False)

print(traktor.show_speed())
print(f"I don`t like your {traktor.color} color. Why not blue?")
