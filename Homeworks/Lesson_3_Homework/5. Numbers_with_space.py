# num_sum = 0
# while True:
#     my_numbers = input('Введите числа через пробел (или введите q для выхода): \n').split()
#     my_simbols = ''.join(my_numbers)
#     if my_simbols.isdigit():
#         num_sum += sum(map(int,my_numbers))
#         print(num_sum)
#     elif my_simbols == 'q':
#         print('Выполнение программы завершено')
#         break
#     else:
#         print('Подумайте ещё\n')
#
# После разбора

def my_func():
    s = 0
    in_list = input('Введите числа через пробел (или введите q для выхода): \n').split()
    for i in in_list:
        if i == 'q':
            return s, True
        try:
            s += int(i)
        except ValueError:
            pass
    return s, False

res = 0
while True:
    a, b = my_func()
    res += a
    print(res)
    if b:
        break
