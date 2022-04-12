# До разбора ДЗ
#____________________________________________________________________
# products = []
# features = {'название': '', 'цена': '', 'количество': '', 'ед': ''}
# analys = {'название': [], 'цена': [], 'количество': [], 'ед': []}
#
# num = 0
#
# feature = None
# control = None
# while True:
#     control = input("Чтобы выйти введите 'Q', чтобы продолжить - 'Enter', чтобы посмотреть аналитику - 'A'").upper()
#     if control == 'Q':
#         break
#     num += 1
#     if control == 'A':
#         print(f'Аналитика \n {"*" * 30}')
#         for key, value in analys.items():
#             print(f'{key[:25]:>30}: {value}')
#             print("*" * 30)
#     for k in features.keys():
#         feature = input(f'Введите "{k}"')
#         features[k] = int(feature) if (k == 'цена' or k == 'количество') else feature
#         analys[k].append(features[k])
#     products.append((num, features))

# После разбора ДЗ
#____________________________________________________________________

i = 1
goods = []
n = int(input('Сколько товаров вы хотите ввести? '))
for _ in range(n):
    print(f'\n {"*" * 30} \n Следующий товар: \n {"*" * 30} \n')
    name = input('Ввведите наименование товара: ')
    price = int(input('Ввведите цену: '))
    quantity = int(input('Ввведите количество: '))
    measure = input('Ввведите единицы измерения: ')

    goods.append((i, {"название": name, "цена": price, "количество": quantity, "ед": measure}))
    i += 1

print(goods)
goods_dict = {"название": [], "цена": [], "количество": [], "ед": []}
for good in goods:
    goods_dict['название'].append(good[1]['название'])
    goods_dict['цена'].append(good[1]['цена'])
    goods_dict['количество'].append(good[1]['количество'])
    if good[1]['ед'] not in goods_dict["ед"]:
        goods_dict['ед'].append(good[1]['ед'])

print(goods_dict)
