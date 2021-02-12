from functools import reduce

num_list = [num for num in range(100, 1001) if num % 2 == 0]
sum = reduce(lambda x, y: x + y, num_list)

print(sum)
