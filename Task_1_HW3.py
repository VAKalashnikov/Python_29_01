def division(a, b):
    if b == 0:
        print("Делить на ноль нельзя")
    else:
        result = a / b
        return result

a = float(input("Введите делимое: "))
b = float(input("Введите делитель: "))

print(division(a, b))
