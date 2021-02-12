my_list = list(map(float, input('Введите числа через пробел: ').split()))

new_list = [i for i, j in zip(my_list[1:], my_list[:-1]) if i > j]

print(new_list)
