my_list = input('Введите слова для списка через пробел \n').split()

for count, el in enumerate(my_list, 1):
    print(count, el[:10])

