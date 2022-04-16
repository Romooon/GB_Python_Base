nums_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [el for el in nums_list if el > nums_list[nums_list.index(el) - 1] and nums_list.index(el) != 0]

print(new_list)