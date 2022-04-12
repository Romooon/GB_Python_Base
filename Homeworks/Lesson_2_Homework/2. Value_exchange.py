n = int(input('Введите количество элементов в списке: \n'))

my_dict = []

for i in range(n):
    m = input()
    my_dict.append(m)

print('До обмена: ', my_dict)

if len(my_dict) % 2 == 0:
    for i in range(0,len(my_dict), 2):
        my_dict[i], my_dict[i+1] = my_dict[i+1], my_dict[i]
else:
    for i in range(0,len(my_dict) - 1, 2):
        my_dict[i], my_dict[i+1] = my_dict[i+1], my_dict[i]

print('После обмена: ', my_dict)


