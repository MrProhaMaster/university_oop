import PySimpleGUI as sg
from math import sqrt

sg.theme('DarkAmber')
layout = [  [sg.Text('Длинна 1 стороны'), sg.InputText(size=10), sg.Button('Сохранить')],
            [sg.Text('Длинна 2 стороны'), sg.InputText(size=10), sg.Text('', key='-TEXT-')],
            [sg.Text('Длинна 3 стороны'), sg.InputText(size=10)],
            [sg.Button('Площадь'), sg.Button('Периметр'), sg.Button('Выйти')]]

win = sg.Window('Triangle Calc', layout, finalize=True)
s = [0, 0, 0]
while True:
    event, values = win.read()
    if event == sg.WIN_CLOSED or event == 'Выйти':
        break
    elif event == 'Сохранить':
        if (int(values[0])+int(values[1]) > int(values[2])) and (int(values[0])+int(values[2]) > int(values[1])) and (int(values[1])+int(values[2]) > int(values[0])):
            s[0] = int(values[0])
            s[1] = int(values[1])
            s[2] = int(values[2])
            win['-TEXT-'].update('Сохранено')
        else:
            sg.popup('Треугольник с такими сторонами не может существовать!')
            win['-TEXT-'].update('')
    elif event == 'Периметр':
        if s[0] > 0 and s[1] > 0 and s[2] > 0:
            sg.popup('Периметр равен: ', s[0]+s[1]+s[2])
        else:
            sg.popup('Сначала сохраните стороны треугольника!')
    elif event == 'Площадь':
        if s[0] > 0 and s[1] > 0 and s[2] > 0:
            p = (s[0]+s[1]+s[2])/2
            summ = p*(p-s[0])*(p-s[1])*(p-s[2])
            sg.popup('Площадь треугольника равна: ', sqrt(summ))
        else:
            sg.popup('Сначала сохраните стороны треугольника!')
