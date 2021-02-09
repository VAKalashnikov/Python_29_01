# Первый пункт задания


def int_func(word):
    c = word[0].upper() + word[1:]
    return c


#print(int_func("need"))

# Вариант для строки

def int_func_str(stroka):
    list_of_words = stroka.split()
    output_list = []
    for one_word in list_of_words:
        c = (one_word[0].upper() + one_word[1:])
        output_list.append(c)
    return " ".join(output_list)

print(int_func_str("протестируем на этой самой строке"))
