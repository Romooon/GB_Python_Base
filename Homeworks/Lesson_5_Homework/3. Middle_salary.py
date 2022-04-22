# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

explo_dict = {}
sal_sum = 0

with open('text_3.txt', 'r', encoding='utf-8') as f:
    for line in f:
        my_key = (line.split())[0]
        my_val = float((line.split())[1])
        explo_dict[my_key] = my_val

print('Меньше 20-ти тысяч получают:')
for key, value in explo_dict.items():
    if value < 20000:
        print(key)
    sal_sum += value

print(f'Средняя зарплата в фирме: {sal_sum / len(explo_dict)} руб.')
