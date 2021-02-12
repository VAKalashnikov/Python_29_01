def fact(n):
    product = 1
    for i in range(1, n + 1):
        product *= i
        yield product


n = int(input("Вам до какого факториала надо?  \n"))
for el in fact(n):
    print("Факториал числа равен {}".format(el))
