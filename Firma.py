# Пятая задача

revenue = float(input("Введите значение выручки фирмы: "))
costs = float(input("Введите значение суммарных издержек фирмы: "))

profit = revenue - costs

if profit > 0:
    print("Вы в плюсе на {} у.е.".format(profit))
    profitability = profit / revenue
    staff = int(input("Сколько у вас работает человек: "))
    print("Каждый сотрудник приносит вам {} прибыли.".format(profit/staff))
elif profit < 0:
    print("Вы в минусе на {} у.е.".format(abs(profit)))
else:
    print("Вы вышли в ноль")

