# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

import math

class Date:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        my_tuple = Date.set_date(self.date)
        day = my_tuple[0]
        month = my_tuple[1]
        year = my_tuple[2]
        return f'Текущая дата: {day}.{month}.{year}'

    @classmethod
    def set_date(cls, date):
        day, month, year = list(map(int, date.split('-')))
        return day, month, year

    @staticmethod
    def valid(day, month, year):
        def calc_month_days(month):
            if month == 2:
                if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
                    return 29
                else:
                    return 28
            else:
                return 30 + (month + month//8) % 2

            # 28 + (month + month//8) % 2 + 2 % month + 1//month * 2 # Работает нормально для невисокосных годов

        if month == 2:
            if day <= calc_month_days(month):
                return 'Всё в порядке'
            else:
                return f'В году {year} в феврале не может быть столько дней: {day}'

        if day <= calc_month_days(month):
            if 1 <= month <= 12:
                return 'Всё в порядке'
            else:
                return 'Такого месяца нет'
        else:
            return f'В месяце {month} не может быть столько дней: {day}'



d1 = Date('29-02-2020')
d2 = Date('29-02-2019')
d3 = Date('31-03-2022')

print(d1)

true_date1 = Date.set_date(d1.date)
print(d1)
print(d1.valid(true_date1[0], true_date1[1], true_date1[2]))

true_date2 = list(Date.set_date(d2.date))
print(d2)
print(d1.valid(true_date2[0], true_date2[1], true_date2[2]))

true_date3 = list(Date.set_date(d3.date))
print(d3)
print(d3.valid(true_date3[0], true_date3[1], true_date3[2]))



