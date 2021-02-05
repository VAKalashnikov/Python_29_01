# Реализуем ввод списка с клавиатуры

input_list = [i for i in input('Введите элементы списка через пробел ').split()]

print(input_list)
print("Ваш список состоит из {} элементов".format(len(input_list)))

index = 0
for i in range(int(len(input_list)/2)):
    input_list[index], input_list[index + 1] = input_list[index + 1], input_list[index]
    index += 2

print(input_list)
