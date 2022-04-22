# 4. Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат.

class Car:
    show_speed = 70

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Авто {self.name} поехало')

    def stop(self):
        print(f'Авто {self.name} остановилось')

    def turn(self, direction):
        print(f'Авто {self.name} повернуло {direction}')

class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)



class WorkCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')

class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


tc = TownCar(41, 'black', 'BMW', False)
sc = SportCar(100, 'red', 'Toyota', False)
wc = WorkCar(61, 'brown', 'Lada', False)
pc = PoliceCar(100, 'white', 'Lamborgini', True)

print(tc.go(), tc.stop(), tc.turn('влево'), tc.show_speed())
print(sc.go(), sc.stop(), sc.turn('вправо'))
print(wc.go(), wc.stop(), wc.turn('влево'), wc.show_speed())
print(pc.go(), pc.stop(), pc.turn('вправо'))
