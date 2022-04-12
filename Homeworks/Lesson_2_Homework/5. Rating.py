my_list = [7, 5, 3, 3, 2]

el = int(input('Введите число: \n'))

if el in my_list:
    my_list.insert((my_list.index(el)), el)
elif el > my_list[0]:
    my_list.insert(0, el)
elif el < my_list[-1]:
    my_list.append(el)

print(my_list)

