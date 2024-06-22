from console import opn, opn2, sec_rep, opn3, onni
from data import authentication

access = authentication()
while access > 0:
    opn(0)
    command = input()
    if command == 'Просмотр данных бортового журнала' or command == '1':
        opn(1)
        new_command = input()
        if new_command == 'Общее состояние станции':
            opn2(1)
        elif new_command == 'Параметры станции':
            sec_rep()
        elif new_command == 'Краткая сводка по бортовому журналу':
            opn2(3)
        elif new_command == 'Краткая выделенная сводка бортового журнала':
            opn2(4)
        elif new_command == 'Подробная сводка бортового журнала':
            opn2(5)
        elif new_command == 'Подробная выделенная сводка бортового журнала':
            opn2(6)
        else:
            print('Введена неизвестная команда')
        print()
        print('Желаете продолжить работу? (Да/Нет)')
        if input() == 'Нет':
            break
        else:
            continue
    elif command == 'Добавление данных в бортовой журнал' or command == '2':
        opn(2)
        new_command = input()
        if new_command == 'Изменение скорости станции':
            opn3(1)
        elif new_command == 'Изменение высоты орбиты станции':
            opn3(2)
        elif new_command == 'Трансфер участников экспедиции':
            opn3(3)
        elif new_command == 'Трансфер груза':
            opn3(4)
        else:
            print('Введена неизвестная команда')
        print()
        print('Желаете продолжить работу? (Да/Нет)')
        if input() == 'Нет':
            break
        else:
            continue

    elif command == 'Редактирование данных в бортовом журнале' or command == '3':
        opn(3)

    elif command == 'Удаление данных из бортового журнала' or command == '4':
        if access != 2:
            print('Недостаточно прав для использования этого режима!')
            continue
        opn(4)
        onni()
    else:
        print('Введена неизвестная команда!')
