class Stationary:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки"


class Pen(Stationary):

    def draw(self):
        return f"Я люблю рисовать ручкой марки {self.title}!"


class Pencil(Stationary):

    def draw(self):
        return f"Я люблю рисовать карандашом марки {self.title}!"

class Handle(Stationary):

    def draw(self):
        return f"Я люблю рисовать маркером марки {self.title}!!"

pen_obj = Pen("Parker")
print(pen_obj.draw())

pencil_obj = Pencil("Brauberg")
print(pencil_obj.draw())

handle_obj = Handle("Stabilo")
print(handle_obj.draw())
