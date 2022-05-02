# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class NullDivision:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return 'Делить на ноль нельзя'

div = NullDivision(10, 100)
print(NullDivision.divide_by_null(114, 0))
print(div.divide_by_null(100, 0))
print(NullDivision.divide_by_null(15, 0.5))
