def my_f(x, y):
    try:
        z = x / y
    except(ZeroDivisionError) as err1:
        print(err1)
        print('На ноль делить нельзя!')

    return z

print(my_f(12, 14))
print(my_f(12, 0))
