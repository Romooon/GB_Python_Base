# def my_f(x, y):
#     try:
#         z = x / y
#     except(ZeroDivisionError) as err1:
#         print(err1)
#         print('На ноль делить нельзя!')
#
#     return z
#
# print(my_f(12, 14))
# print(my_f(12, 0))

# После проверки

def div(x, y):
    try:
        return int(x) / int(y)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')
    except ValueError:
        print('Введите целые числа')


print(div(input('Введите первое число: '),input("А теперь второе: ")))
