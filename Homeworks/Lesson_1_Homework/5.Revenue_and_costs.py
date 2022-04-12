revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))

if revenue > costs:
    print('Прибыль есть')
    profit = revenue - costs
    profitability = (profit / revenue) * 100
    print(f'Рентабельность: {profitability} %')
    emloyees = int(input('Сколько у вас работников? '))
    em_prof = profit / emloyees
    print(f'Прибыль с одного работника: {em_prof}')
elif revenue < costs:
    print('Убыток')

else:
    print('Вы вышли в ноль!')
