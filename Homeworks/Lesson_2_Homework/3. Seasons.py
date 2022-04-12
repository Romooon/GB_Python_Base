# вариант со списком

summer = [6,7,8]
autumn = [9,10,11]
winter = [12,1,2]
spring = [3,4,5]

while True:
    n = int(input('[list_task] Введите номер месяца: \n'))

    if n in summer:
        print('Лето')
        break
    elif n in autumn:
        print('Осень')
        break
    elif n in spring:
        print('Весна')
        break
    elif n in winter:
        print('Зима')
        break
    else:
        print('Такого месяца нет, подумайте ещё')
        break


# вариант со словарём

n = int(input('{dict_task} Введите номер месяца: \n'))

seasons = {
    'Лето': [6,7,8],
    'Осень': [9,10,11],
    'Зима': [12,1,2],
    'Весна': [3,4,5]
}
for key, value in seasons.items():
    if n in value:
        print(key)
