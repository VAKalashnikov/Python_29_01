f = open("text.txt", "r")
str_list = []

for line in f:
    print(line, end="")
    str_list.append(line)

print()
print("В вашем файле {} строк(и)".format(len(str_list)))
print()

# А теперь будем считать кол-во слов в каждой строке
s = []
for i in range(len(str_list)):
    print("В {}-ой строке файла имеется {} слов(а)".format(i + 1, len(str_list[i].split())))

f.close()
