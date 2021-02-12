# Нужно запускать в терминале
from sys import argv

name, virabotka, stavka, premiya = argv

print("Ваша зарплата:", float(virabotka) * float(stavka) + float(premiya))
