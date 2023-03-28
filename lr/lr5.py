class empl:
    def __init__(self):
        self.number = 0
        self.salary = 0
    def input_(self):
        self.number = input("Введите номер сотрудника: ")
        self.salary = input("Введите оклад сотрудника: ")
    def __str__(self):
        return f'Номер сотрудника: {self.number};\n Оклад сотрудника: {self.salary}.'

def t2():
    empl1 = empl()
    empl1.input_()
    print(empl1)