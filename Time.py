# Вторря задача
user_sec = int(input("Введите время в секундах: "))

new_seconds = user_sec % (24 * 3600)
hours = new_seconds // 3600
minutes = (new_seconds - hours * 3600) // 60
seconds = new_seconds % 60

print("Время на цифорвых часах: {:02d}:{:02d}:{:02d}.".format(hours, minutes, seconds))

