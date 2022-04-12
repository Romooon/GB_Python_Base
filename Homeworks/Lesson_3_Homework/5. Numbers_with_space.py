num_sum = 0
while True:
    my_numbers = input('Введите числа через пробел (или введите q для выхода): \n').split()
    my_simbols = ''.join(my_numbers)
    if my_simbols.isdigit():
        num_sum += sum(map(int,my_numbers))
        print(num_sum)
    elif my_simbols == 'q':
        print('Выполнение программы завершено')
        break
    else:
        print('Подумайте ещё\n')

