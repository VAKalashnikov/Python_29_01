def myfunc(a, b, c):
    numbers = [a, b, c]
    numbers.remove(min(numbers))
    return sum(numbers)


try:
    a, b, c = input("Введите три числа через пробел: ").split()
    print(myfunc(float(a), float(b), float(c)))
except:
    print("Я просил три значения, через пробел(((")
