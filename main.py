# Функция приветствия при запуске
def welcome():
    print('-----------------------------')
    print('-----------И Г Р А-----------')
    print('-------К Р Е С Т И К И-------')
    print('---------П Р О Т И В---------')
    print('--------Н О Л И К О В--------')
    print('-----------------------------')
    print('---------Инструкция:---------')
    print('-Для выбора клетки для хода--')
    print('----введите через пробел-----')
    print('---------два числа:----------')
    print('--первое число - для строки--')
    print('--второе число - для столбца-')
    print('-----------------------------')
    print('-------У Д А Ч И ! ! !-------')
    print('-----------------------------')


# Функция прорисовки игрового поля
def draw_field():
    print('   0 1 2')
    for i in range(len(field)):
        print(str(i) + '|', *field[i])


# Функция проверки вводимых координат на качество данных
def step_check(x_or_0):
    while True:
        XY = input(f'Сейчас ходит {x_or_0}. Введите координаты клетки: ').split()

        if len(XY) != 2:
            print('Кажется вы ввели не 2 числа! Попробуйте еще раз.')
            continue
        else:
            x, y = XY

        if not (x.isdigit() and y.isdigit()):
            print('Вы ввели не числа! Попробуйте ещё раз.')
            continue
        else:
            x, y = int(x), int(y)

        if not (0 <= x <= 2) or not (0 <= y <= 2):
            print('Координаты выходят за границы поля! Попробуйте ещй раз.')
            continue

        if field[x][y] != ' ':
            print('Эта клетка уже занята! Выберите другую.')
            continue

        return x, y


# Функция проверки на победу
def win_check(side):
    win_conditions = (((0, 0), (0, 1), (0, 2)),
                      ((1, 0), (1, 1), (1, 2)),
                      ((2, 0), (2, 1), (2, 2)),
                      ((0, 0), (1, 0), (2, 0)),
                      ((0, 1), (1, 1), (2, 1)),
                      ((0, 2), (1, 2), (2, 2)),
                      ((0, 0), (1, 1), (2, 2)),
                      ((2, 0), (1, 1), (0, 2)))
    for variant in win_conditions:
        L = []
        for xy in variant:
            L.append(field[xy[0]][xy[1]])
        if L == [side, side, side]:
            return True
    return False


# Основная функция для обработки ходов
def game(count):
    while True:
        draw_field()
        count += 1

        if count % 2 == 1:
            side = 'X'
        else:
            side = '0'

        if count < 10:
            x, y = step_check(side)
            field[x][y] = side

        if win_check(side):
            draw_field()
            print(f'Победил {side}!')
            break

        elif count == 10:
            print('Игра закончена! Ничья.')
            break


welcome()

count = 0  # Счётчик ходов

# Основной цикл для обработки хода игры
while True:
    field = [[' ' for x in range(3)] for y in range(3)]
    game(count)
    print('Хотите сыграть ещё раз?')
    answer = input('Если ДА - нажмите кнопку 1. Если нет - любую другую: ')
    if answer =='1':
        count = 0
    else:
        print('До свидания!')
        break
