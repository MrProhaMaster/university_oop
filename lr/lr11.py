class employee:
    def __init__(self):
        self.num = 0
        self.salary = 0

    def input(self):
        self.num = input('Введите номер сотрудника: ')
        self.salary = input('Введите оклад сотрудника: ')

    def __str__(self):
        return f'Сотрудник под номером {self.num} с окладом {self.salary}'

def lr11():
    e1 = employee()
    e2 = employee()
    e3 = employee()
    l = [e1, e2, e3]
    for i in l:
        i.input()
    for i in l:
        print(i)