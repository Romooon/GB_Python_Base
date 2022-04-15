# def exponent(x, y):
#     res = x ** y
#     return res
#
# print(exponent(10, -2))

# После проверки

def my_func(x, y ):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print('Программа работает только с действительными x и целыми у')
        return
    if x <= 0 or y >= 0:
        print('Программа работает только с положительными x и отрицательными у')
        return
    return x ** y

print(my_func(1, 2))
