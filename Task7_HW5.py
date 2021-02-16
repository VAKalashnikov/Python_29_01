import json


# начнем с того, что применим функцию из предыдущего задания для получения чисел из строки

def read_integers(line):
    num = ''
    num_list = []
    for char in line:
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                num_list.append(int(num))
                num = ''
    if num != '':
        num_list.append(int(num))
    return num_list


with open("firma.txt", "r") as f:
    revenue = []
    s = []
    company = []
    for line in f:
        company.append(line.split()[0])
        s = read_integers(line)
        revenue.append(s[1] - s[2])
    mean_revenue = sum(revenue) / len(revenue)  # считаем среднюю прибыль
    comp_rev = {i: j for i, j in zip(company, revenue)}  # создаем словарь с компаниями
    average_dict = {"average profit": mean_revenue}
    final_dict = [comp_rev]
    final_dict.append(average_dict)
    print(final_dict)

# восхитительно, осталось только преобразовать в json

with open("final_dict.json", "w") as write_f:
    json.dump(final_dict, write_f)
