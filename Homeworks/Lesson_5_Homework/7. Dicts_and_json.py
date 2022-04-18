# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

firms = {}
av_prof = {}
sum_prof = 0
prof_firms = 0
with open('text_7.txt', 'r', encoding='utf-8') as s:
    for l in s:
        firm = (((l).strip('\n')).split())
        profit = int(firm[-2]) - int(firm[-1])
        firms[firm[0]] = profit

for val in firms.values():
    if val > 0:
        sum_prof += val
        prof_firms += 1

average_profit = sum_prof / prof_firms
av_prof['average_profit'] = average_profit
final_list = [firms, av_prof]
print(final_list)

with open('final_list_7.json','w', encoding='utf-8') as f:
    json.dump(final_list, f, ensure_ascii=False, indent=4)
