def my_func(a, b, c):
    num_list = [a, b, c]
    del num_list[num_list.index(min(num_list))]
    num_sum = sum(num_list)

    return num_sum

print(my_func(82,8,6))