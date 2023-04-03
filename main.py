from lr.lr4 import t1 as l1t1, t2 as l1t2, t3 as l1t3, t4 as l1t4
from lr.lr5 import t2 as l2t2
from lr.lr6 import t1 as l3t1, t2 as l3t2, t3 as l3t3, t4 as l3t4
from lr.lr7 import lr7

while True:
    in_ = input("Введите номер практического занятия (от 4 до 7), которое необходимо запустить (для выхода введите q): ")
    if in_ == '4':
        while True:
            in_ = input("Введите номер задания: ")
            if in_ == '1':
                l1t1()
            elif in_ == '2':
                l1t2()
            elif in_ == '3':
                l1t3()
            elif in_ == '4':
                l1t4()
            elif in_ == 'q':
                break
            else:
                print('Введен некорректный номер задачи!')

    elif in_ == '5':
        while True:
            in_ = input("Введите номер задания: ")
            if in_ == '1':
                print("Структуры переделаны в классы.")
            elif in_ == '2':
                l2t2()
            elif in_ == 'q':
                break
            else:
                print('Введен некорректный номер задачи!')

    elif in_ == '6':
        while True:
            in_ = input("Введите номер задания: ")
            if in_ == '1':
                l3t1()
            if in_ == '2':
                l3t2()
            if in_ == '3':
                l3t3()
            if in_ == '4':
                l3t4()
            if in_ == '5':
                print("Сделано")
            elif in_ == 'q':
                break
            else:
                print('Введен некорректный номер задачи!')

    elif in_ == '7':
        lr7()

    elif in_ == 'q':
        break

    else:
        print('Введена некоректная команда!')