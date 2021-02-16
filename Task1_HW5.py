lines = input("Введите текст: (строки через пробел)").split()

with open("new.txt", "w") as file:
    for line in lines:
        file.write(line + '\n')
