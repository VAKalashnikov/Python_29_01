# Шестая задача

# Сделал в виде функции

def run(a, b):
    total_dist = 0
    day_counter = 0
    while total_dist < b:
        total_dist = total_dist + a * (1.1 ** day_counter)
        day_counter += 1
    return day_counter


