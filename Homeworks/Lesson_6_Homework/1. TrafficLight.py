# 1. Создать класс TrafficLight (светофор).
# ● определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт.

from time import sleep

class TrafficLight:
    __color = 'Красный'

    def running(self, count, red_time, yellow_time, green_time):
        while count > 0:
            self.__color = 'Красный'
            print(f'\033[31m{self.__color}')
            for i in range(1, red_time + 1):
                sleep(1)
                print(f'\033[31m{i} сек')

            self.__color = 'Жёлтый'
            print(f'\033[33m{self.__color}')
            for i in range(1, yellow_time + 1):
                sleep(1)
                print(f'\033[33m{i} сек')

            self.__color = 'Зелёный'
            print(f'\033[32m{self.__color}')
            for i in range(1, green_time + 1):
                sleep(1)
                print(f'\033[32m{i} сек')

            count -= 1

t = TrafficLight()
t.running(3,7,2,7)
