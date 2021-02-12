# сделаем пункт а

from itertools import count

num = input("Введите начальный элемент(натуральное число): ")
final_num = input("Введите конечный элемент (натуральное число, большее введенного ранее): ")

try:
    for i in count(int(num)):
        if i > int(final_num): # последний элемент сгенерированного списка
            break
        else:
            print(i, end = " ")
except ValueError:
    print("Вы ввели не то")

# а это уже пункт б (лень реализовывать ввод)

from itertools import cycle

count = 1
for letter in cycle('АБВГД'):
    if count > 6:  # Здесь нужно задать число элементов последовательности
        break
    print(letter)
    count += 1
