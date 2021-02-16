# сначала напишем функцию, которая считывает в строке только числа (хотя бы целые, как в нашей задаче)

def read_integers(line):  # немного подглянул в интернете
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

# ну а теперь все довольно просто

with open('ucheba.txt', 'r', encoding="utf-8") as f:
    line_sum = []
    subjects = []
    for line in f:
        line_sum.append(sum(read_integers(line)))
        subjects.append(line.split()[0][:-1])

# отлично, все готово, (возможно, немного коряво) осталось сшить все в словарь

    subject_hours = {i: j for i, j in zip(subjects, line_sum)}
    print(subject_hours)
