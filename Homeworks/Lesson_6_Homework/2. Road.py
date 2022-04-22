# 2. Реализовать класс Road (дорога).
# ● определить атрибуты: length (длина), width (ширина);
# ● значения атрибутов должны передаваться при создании экземпляра класса;
# ● атрибуты сделать защищёнными;
# ● определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# ● использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра
# дороги асфальтом, толщиной в 1 см*число см толщины полотна;
# ● проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def culc_weight(self, thickness, sq_weight):
        print(self._length)
        print(self._width)
        print(thickness)
        print(sq_weight)

        return self._length * self._width * sq_weight * thickness

r = Road(100, 4)
print(f'{(r.culc_weight(7, 25))/1000} т асфальта необходимо для строительства дороги')
