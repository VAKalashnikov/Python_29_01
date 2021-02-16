translator = {"One": "Один",
              "Two": "Два",
              "Three": "Три",
              "Four": "Четыре"}

changes = []
with open('english.txt', 'r') as f:
    for i in f:
        i = i.split(' ', 1)
        changes.append(translator[i[0]] + '  ' + i[1])

with open('english.txt', 'w') as f_new:
    f_new.writelines(changes)
