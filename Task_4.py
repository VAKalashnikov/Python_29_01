text = input("Введите текст: ")

text = text.split(" ")
str_count = 1

for word in text:
    print(str_count, word[:10])
    str_count += 1
