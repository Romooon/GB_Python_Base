# 1) Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

from copy import deepcopy

my_list1 = [[7, 8, 9],
           [4, 5, 6],
           [1, 2, 3]]
my_list2 = [[98, 8, 9],
           [4, 4, 1],
           [0, 2, 75]]
my_list3 = [[7, 8, 9, 10],
           [4, 5, 6, 81]]

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        y = ''
        for i in self.matrix:
            y = y + ' '.join(str(x) for x in i) + '\n'
        return y

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return 'Складывать между собой можно только матрицы с одинаковым размером\n'
        new_matrix = deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for n in range(len(self.matrix[i])):
                new_matrix[i][n] = self.matrix[i][n] + other.matrix[i][n]
        return Matrix(new_matrix)

m1 = Matrix(my_list1)
m2 = Matrix(my_list2)
m3 = Matrix(my_list3)

print(m1)
print(m2)
print(m3)

m4 = m1 + m3
m5 = m1 + m2
print(m4)
print(m5)

