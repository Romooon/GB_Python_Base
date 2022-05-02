# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А
# также класс «Оргтехника», который будет базовым для классов-наследников. Эти классы —
# конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# ____________________________________________________________________________________________
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники
# на склад и передачу в определенное подразделение компании. Для хранения данных
# о наименовании и количестве единиц оргтехники, а также других данных, можно использовать
# любую подходящую структуру, например словарь.
# ______________________________________________________________________________________________
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых
# пользователем данных. Например, для указания количества принтеров, отправленных на
# склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Store:

    def __init__(self, name, price, quantity, sheets, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.sheets = sheets
        self.my_store_full = []
        self.my_store = []
        self.goods = {'Наименование': self.name, 'Цена': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name}. Цена: {self.price}, количество: {self.quantity} \n'

    def reception(self):
        try:
            name = input(f'Введите наименование ')
            price = int(input(f'Введите цену за ед '))
            quan = int(input(f'Введите количество '))
            item = {'Наименование': name, 'Цена': price, 'Количество': quan}
            self.goods.update(item)
            self.my_store.append(self.goods)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка при вводе данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input('>>> ').lower()
        if q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return 'Выход'
        else:
            return Store.reception(self)


class Printer(Store):
    def to_print(self):
        return f'Печатает со скоростью {self.sheets} в минуту'


class Scanner(Store):
    def to_scan(self):
        return f'Сканирует со скоростью {self.sheets} в минуту'


class Copier(Store):
    def to_copier(self):
        return f'Копирует со скоростью {self.sheets} в минуту'


good1 = Printer('Epson 3011', 2000, 5, 10)
good2 = Scanner('Canon - 210x', 1200, 5, 10)
good3 = Copier('Xerox WorkCetntre 3245', 1500, 1, 15)
print(good1.reception())
print(good2.reception())
print(good3.reception())

print(good1.to_print())
print(good2.to_scan())
print(good3.to_copier())