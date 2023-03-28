class Tile:
    def __init__(self):
        self.brand = ''
        self.size_h = 0
        self.size_w = 0
        self.price = 0

    def getData(self):
        self.brand = input('Введите брэнд: ')
        self.size_h = input('Введите размер (высоту): ')
        self.size_w = input('Введите размер (ширину): ')
        self.price = input('Введите цену: ')
    def __str__(self):
        return f'Брэнд плитки: {self.brand};\nВысота плитки: {self.size_h};\nШирина плитки: {self.size_w};\nЦена плитки: {self.price}\n'

class Children:
    def __init__(self):
        self.__name__ = ''
        self.__surname__ = ''
        self.__age__ = 0
    def input_(self):
        self.__name__ = input('Введите имя: ')
        self.__surname__ = input('Введите фамилию: ')
        self.__age__ = input('Введите возраст: ')
    def __str__(self):
        return f'Имя ребенка: {self.__name__};\nФамилия ребенка: {self.__surname__};\nВозраст ребенка: {self.__age__}'

class p3t3c:
    def __init__(self):
        self.num = 0

    def input_(self, ch):
        self.num = ch

    def __str__(self):
        return self.num

def t1():
    tile1 = Tile()
    tile2 = Tile()
    tile1.getData()
    tile2.getData()
    print(tile1, tile2)

def t2():
    ch1 = Children()
    ch1.input_()
    print(ch1)

def t3():
    num1 = p3t3c
    num2 = p3t3c
    num3 = p3t3c
    num1.input_(6)
    num2.input_(109)
    num3.input_(input('Введите число: '))
    print(num1, num2, num3)

def t4():
    while True:
        l = []
        in_ = input('Хотите добавить нового сотрудника? (y/n): ')
        if in_ == 'y':
            add = empl()
            add.input_()
        elif in_ == 'n':
            break
        else:
            print('Неизвестная команда!')