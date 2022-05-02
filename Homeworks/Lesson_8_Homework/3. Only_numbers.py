# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на
# наличие только чисел. Проверить работу исключения на реальном примере. Запрашивать у
# пользователя данные и заполнять список необходимо только числами. Класс-исключение
# должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
# пользователь сам не остановит работу скрипта, введя, например, команду «stop». При этом
# скрипт завершается, сформированный список с числами выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа
# элемента. Вносить его в список, только если введено число. Класс-исключение должен не
# позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

# my_list = []
# el = ''
# while True:
#     el = input('Введите число или "stop", чтобы остановиться \n')
#     try:
#         el = int(el)
#     except:
#
#     if el == 'stop':
#         break
#     my_list.append(el)
#
# print(my_list)

class MyError:
    def __init__(self, *args):
        self.my_list = []

    def user_input(self):
        while True:
            try:
                el = int(input('Введите число \n'))
                self.my_list.append(el)
            except:
                print('Строка и булево не должны добавляться в список')
                question = input('Продолжить? (да, нет) \n').lower()

                if question == 'да':
                    self.user_input()
                else:
                    return 'Выполнение программы завершено'
                    break

my_err = MyError()
print(my_err.user_input())