rating = [7, 5, 3, 3, 2]

k = int(input("Введите новый элемент рейтинга: "))
count = 0

# Проверим есть ли такое число в рейтинге

if k in rating:
    i = rating.index(k)
    rating.insert(i + 1, k)
else:
    for i in range(len(rating)):
        if rating[i] < k:
            rating.insert(i, k)
            break
        else:
            rating.append(k)
            break

print(rating)
