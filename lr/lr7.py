from math import pi

class Cylinder:
    def __init__(self, h, r):
        self.h = h
        self.r = r

    def __str__(self):
        return f'Цилиндр:\nВысота - {self.h};\nРадиус - {self.r};\n'

    def V(self):
        print(f'Объем цилиндра = {pi*(self.r**2)*self.h};\n')

    def SO(self):
        print(f'Площадь основания = {pi*self.r**2};\n')

    def SB(self):
        print(f'Площадь боковой поверхности = {2*pi*self.r*self.h};\n')

def lr7():
    h = int(input('Введите высоту цилиндра: '))
    r = int(input('Введите радиус цилиндра: '))
    cyl = Cylinder(h, r)
    while True:
        in_ = input('Выберите операцию: \nВычислить объем цилиндра - 1;\nВычислить площадь основания - 2;\nВычислить площадь боковой поверхности цилиндра - 3;\nВыйти - q;\n')
        if in_ == '1':
            cyl.V()
        elif in_ == '2':
            cyl.SO()
        elif in_ == '3':
            cyl.SB()
        elif in_ == 'q':
            break
        else:
            print('Введена некорректная комманда!')
