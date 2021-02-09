def negative_power(x, y):
    x = 1/x
    y = -y
    result = 1
    while y > 0:
        result *= x
        y -= 1
    return result


x = float(input("Введите дейтсвительное число: "))
y = int(input("Введите целую отрицательную степень: "))
print(negative_power(x, y))
