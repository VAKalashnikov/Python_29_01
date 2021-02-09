def user_data(**data):
    for key, info in data.items():
        print(f"{key}: {info}")


name = input("Введите свое имя: ")
surname = input("Введите фамилию: ")
birth_year = input("В каком году вы родились? ")
location = input("В каком городе вы проживаете? ")
email = input("Введите электронную почту: ")

print(user_data(Name=name, Surname=surname, Birth_year=birth_year, Location=location, Email=email))
