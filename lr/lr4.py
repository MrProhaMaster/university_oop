class part:
    def __init__(self, modelnumber, partnumber, cost):
        self.modelnumber = modelnumber
        self.partnumber = partnumber
        self.cost = cost

class phone:
    def __init__(self, part1, part2, part3):
        self.part1 = part1
        self.part2 = part2
        self.part3 = part3

class time:
    def __init__(self, hours, minutes, second):
        self.hours = hours
        self.minutes = minutes
        self.second = second
    def seconds(self):
        print(f"Количество секунд: {(self.hours*60*60) + (self.minutes*60) + (self.second)}")

class tovar:
    def __init__(self, rubles, kops):
        self.rubles = rubles
        self.kops = kops
        self.cost = self.rubles + self.kops

def t1():
    part1 = part(6244, 373, 217.55)
    part2 = part1
    print(f"model {part1.modelnumber}\ndetal {part1.partnumber}\nStoimost {part1.cost}\n\nmodel {part2.modelnumber}\ndetal {part2.partnumber}\nStoimost {part2.cost}")

def t2():
        number = []
        print("Введите код города, номер станции и номер абонента: ")
        for i in range(3):
            n = int(input())
            number.append(n)
        phone1 = phone(212, 767, 8900)
        phone2 = phone(number[0], number[1], number[2])
        print(f"Мой номер: ({phone1.part1}) {phone1.part2}-{phone1.part3}\nВаш номер: ({phone2.part1}) {phone2.part2}-{phone2.part3}")

def t3():
    h = int(input("Введите количество часов: "))
    m = int(input("Введите количество минут: "))
    s = int(input("Введите количество секунд: "))
    time1 = time(h, m ,s)
    time1.seconds()

def t4():
    tovar1 = tovar(100, 0)
    tovar2 = tovar(150, 50)
    tovar3 = tovar(200, 0)
    tovar4 = tovar(70, 99)
    t1 = input("Список товаров: tovar1, tovar2, tovar3, tovar4;\nВведите номер первого товара для сравнения: ")
    if t1 == '1':
        t2 = input("Список товаров для сравнения: tovar2, tovar3, tovar4;\nВведите номер второго товара для сравнения: ")
        if t2 == '2':
            if tovar1.cost > tovar2.cost:
                print(f"tovar1({tovar1.cost}) дороже tovar2({tovar2.cost})")
            else:
                print(f"tovar2({tovar2.cost}) дороже tovar1({tovar1.cost})")
        elif t2 == '3':
            if tovar1.cost > tovar3.cost:
                print(f"tovar1({tovar1.cost}) дороже tovar3({tovar3.cost})")
            else:
                print(f"tovar3({tovar3.cost}) дороже tovar1({tovar1.cost})")
        elif t2 == '4':
            if tovar1.cost > tovar4.cost:
                print(f"tovar1({tovar1.cost}) дороже tovar4({tovar4.cost})")
            else:
                print(f"tovar4({tovar4.cost}) дороже tovar1({tovar1.cost})")
    elif t1 == '2':
        t2 = input("Список товаров для сравнения: tovar1, tovar3, tovar4;\nВведите номер второго товара для сравнения: ")
        if t2 == '1':
            if tovar1.cost > tovar2.cost:
                print(f"tovar1({tovar1.cost}) дороже tovar2({tovar2.cost})")
            else:
                print(f"tovar2({tovar2.cost}) дороже tovar1({tovar1.cost})")
        elif t2 == '3':
            if tovar3.cost > tovar2.cost:
                print(f"tovar3({tovar3.cost}) дороже tovar2({tovar2.cost})")
            else:
                print(f"tovar2({tovar2.cost}) дороже tovar3({tovar1.cost})")
        elif t2 == '4':
            if tovar4.cost > tovar2.cost:
                print(f"tovar4({tovar4.cost}) дороже tovar2({tovar2.cost})")
            else:
                print(f"tovar2({tovar2.cost}) дороже tovar4({tovar4.cost})")
    elif t1 == '3':
        t2 = input("Список товаров для сравнения: tovar1, tovar2, tovar4;\nВведите номер второго товара для сравнения: ")
        if t2 == '1':
            if tovar1.cost > tovar3.cost:
                print(f"tovar1({tovar1.cost}) дороже tovar3({tovar3.cost})")
            else:
                print(f"tovar3({tovar3.cost}) дороже tovar1({tovar1.cost})")
        elif t2 == '2':
            if tovar3.cost > tovar2.cost:
                print(f"tovar3({tovar3.cost}) дороже tovar2({tovar2.cost})")
            else:
                print(f"tovar2({tovar2.cost}) дороже tovar3({tovar3.cost})")
        elif t2 == '4':
            if tovar3.cost > tovar4.cost:
                print(f"tovar3({tovar3.cost}) дороже tovar4({tovar4.cost})")
            else:
                print(f"tovar4({tovar4.cost}) дороже tovar3({tovar3.cost})")
    elif t1 == '4':
        t2 = input("Список товаров для сравнения: tovar1, tovar2, tovar3;\nВведите номер второго товара для сравнения: ")
        if t2 == '1':
            if tovar1.cost > tovar4.cost:
                print(f"tovar1({tovar1.cost}) дороже tovar4({tovar4.cost})")
            else:
                print(f"tovar4({tovar4.cost}) дороже tovar1({tovar1.cost})")
        elif t2 == '2':
            if tovar2.cost > tovar4.cost:
                print(f"tovar2({tovar2.cost}) дороже tovar4({tovar4.cost})")
            else:
                print(f"tovar4({tovar4.cost}) дороже tovar2({tovar2.cost})")
        elif t2 == '3':
            if tovar3.cost > tovar4.cost:
                print(f"tovar3({tovar3.cost}) дороже tovar4({tovar4.cost})")
            else:
                print(f"tovar4({tovar4.cost}) дороже tovar3({tovar3.cost})")