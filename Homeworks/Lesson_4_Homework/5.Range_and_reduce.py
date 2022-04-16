from functools import reduce

def expo(var1, var2):
    return var1 * var2

my_list = [el for el in range(100, 1001) if el % 2 != 0]
res = reduce(expo, my_list)

print(res)