f = open("trud.txt", 'r')
str_list = []

for line in f:
    str_list.append(line.split())

# print(str_list)

# Для простоты сделаем из этих данных словарь

key = [str_list[i][0] for i in range(len(str_list))]
value = [float(str_list[i][1]) for i in range(len(str_list))]

salary_dict = {k:v for k, v in zip(key, value)}
# print(salary_dict)
for surname in salary_dict.keys():
    if salary_dict.get(surname) < 20:
        print("У сотрудника {} зарпалата меньше 20 тысяч.".format(surname))

mean_solary = sum(value)/len(value)
print("Средняя зарплата сотрудника равна ", mean_solary)