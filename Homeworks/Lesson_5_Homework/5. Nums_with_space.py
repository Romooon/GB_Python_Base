# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
with open('Nums5.txt', 'w+', encoding='utf-8') as n:
    n.writelines('4 5 6 3 6 3 6 3 8 9 8 1 5 2 5 8')

with open('Nums5.txt', 'r', encoding='utf-8') as n:
    num_list = list(map(int,((n.readlines())[0]).split()))
    print(sum(num_list))

