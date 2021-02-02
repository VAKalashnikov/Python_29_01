# Четвертая задача

num = int(input("Введеите натуральное число: "))
greatest_figure = 0

while num > 0:
    last_figure = num % 10
    if last_figure > greatest_figure:
        greatest_figure = last_figure
    num = (num - last_figure) // 10

print("Самая ольшая цифра в вашем числе: ", greatest_figure)
