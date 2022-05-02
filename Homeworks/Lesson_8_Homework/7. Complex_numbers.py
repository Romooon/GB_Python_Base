# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
# работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните
# сложение и умножение созданных экземпляров. Проверьте корректность полученного
# результата.

class ComplexNumber:
    def __init__(self, com_num):
        self.com_num = complex(com_num)

    def __str__(self):
        return str(self.com_num)

    def __add__(self, other):
        return ComplexNumber(self.com_num + other.com_num)

    def __radd__(self, other):
        if not isinstance():
            return self
        return self.__add__(other)

    def __sub__(self, other):
        return ComplexNumber(self.com_num - other.com_num)


    def __mul__(self, other):
        return ComplexNumber(self.com_num * other.com_num)

    def __truediv__(self, other):
        return ComplexNumber(self.com_num / other.com_num)




com1 = ComplexNumber('3+4j')
com2 = ComplexNumber('2-1j')
com3 = com1 + com2 + com1
com4 = com1 - com2
com5 = com1 * com2
com6 = com1 / com2

print(com3)
print(com4)
print(com5)
print(com6)


