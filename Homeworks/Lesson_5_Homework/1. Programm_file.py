# 1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.

# with open('program_file.txt', 'w', encoding='utf-8') as pf:
#     my_str = None
#     while not my_str == '':
#         my_str = input('Поочерёдно вводите строки для записи (Для выхода нажмите Enter): ')
#         pf.writelines(my_str + '\n')
#
# После проверки

# with open('program_file.txt', 'w', encoding='utf-8') as f:
#     while True:
#         line = input('Введите текст, для выхода Enter: ')
#         if not line:
#             break
#         print(line, file=f)

# Ещё вариант
#
print('Введите данны для записи в файл. \nДля окончания ввода введите пустую строку')
with open('program_file.txt', 'w', encoding='utf-8') as my_f:
    while (line := input("Введите строку: ")) != '':
        my_f.write(f"{line}\n")
