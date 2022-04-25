# 3) Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо
# создать класс Клетка. В его конструкторе инициализировать параметр, соответствующий
# количеству ячеек клетки (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только
# к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением
# до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться
# сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и
# количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n
# равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний
# ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод
# make_order() вернет строку: *****\n*****\n*****.

class Cell:

    def __init__(self, quan):
        self.quan = quan

    def __str__(self):
        return f'Количество ячеек в клетке: {self.quan}'

    def __add__(self, other):
        return self.quan + other.quan

    def __sub__(self, other):
        my_sub = self.quan - other.quan
        return my_sub if my_sub > 0 else 'Разность должна быть больше нуля'


    def __mul__(self, other):
        new_cell = self.quan * other.quan
        return Cell(new_cell)

    def __truediv__(self, other):
        new_cell = round(self.quan / other.quan)
        return Cell(new_cell)

    def make_order(self, quan_range):
        my_list = []
        y = ''
        for i in range(self.quan // quan_range):
            my_list.append('*' * quan_range)
        my_list.append('*' * (self.quan % quan_range))

        for i in my_list:
            y = y + ''.join(str(x) for x in i) + '\n'

        return y

c1 = Cell(15)
c2 = Cell(12)
c3 = c1 * c2
c4 = c1 / c2
print(c3)
print(c4)
print(c1.make_order(7))
