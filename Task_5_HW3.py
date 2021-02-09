def repeat_summation():
    summa = 0
    while True:
        numbers = input('Введите набор чисел или * для выхода: ').split()
        for i in numbers:
            try:
                if i == '*':
                    print(f'Сумма равна {summa}.')
                    return
                else:
                    summa += float(i)
            except ValueError:
                print('Введите набор чисел или * для выхода *')
        print(f'Сумма равна {summa}')

repeat_summation()
