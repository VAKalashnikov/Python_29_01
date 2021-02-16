f = open("count.txt", 'w')

num_line = input("Введите набор чисел разделенных пробелами: ")
f.writelines(num_line)


try:
    num_list = list(map(float, num_line.split()))
    print("Сумма чисел в наборе, записанном в файле равна", sum(num_list))
except:
    print("Вы ввели неправильно")

f.close()