field = [["-" for j in range(3)] for i in range(3)]


# функция для инструкции к игре
def instruction():
    print("*" * 3, ''' Привет! Это игра "Крестики-нолики"''', "*" * 3)
    print('''Чтобы сделать ход, введи координаты клетки, 
куда хочешь поставить свой символ("x" или "o"). 
Первый ход делает игрок, ставящий крестики.''')


# функция для отрисовки поля
def draw_field(f):
    print("  0 1 2")
    for i in range(len(field)):
        print(str(i), *field[i])


# функция, которая принимает координаты от пользователяи и
# проверяет корректность их ввода
def users_input(f):
    while True:
        cell_coordinates = input("Введите координаты клетки через пробел: ").split()
        if len(cell_coordinates) != 2:
            print("Некорректный ввод. Введите две координаты клетки через пробел.")
            continue
        if not (cell_coordinates[0].isdigit() and cell_coordinates[1].isdigit()):
            print("Некорректный ввод. Введите числа.")
            continue
        x, y = map(int, cell_coordinates)
        if not (0 <= x < 3 and 0 <= y < 3):
            print("Некорректный ввод. Вышли из диапазона.")
            continue
        if f[x][y] in "xo":
            print("Клетка уже занята")
            continue
        break
    return x, y


# функция проверки выигрыша
def check_win(f, symbol):
    def check_line(cell_1, cell_2, cell_3, s):
        if cell_1 == s and cell_2 == s and cell_3 == s:
            return True

    for n in range(3):
        if check_line(f[n][0], f[n][1], f[n][2], symbol) or \
                check_line(f[0][n], f[1][n], f[2][n], symbol) or \
                check_line(f[0][0], f[1][1], f[2][2], symbol) or \
                check_line(f[0][0], f[1][0], f[2][0], symbol):
            return True


instruction()


def main(f):
    counter = 0
    while True:
        if counter % 2 == 0:
            symbol = "x"
        else:
            symbol = "o"
        print("")
        draw_field(field)
        print(f"Ход игрока {symbol}")
        x, y = users_input(field)
        field[x][y] = symbol
        counter += 1
        if counter > 4:
            win = check_win(field, symbol)
            if win:
                draw_field(field)
                print(" ")
                print(f"Выиграл {symbol}. Поздравляем!")
                break
        if counter == 9:
            draw_field(field)
            print(" ")
            print("Ничья")
            break

    restart = input("Хотите сыграть ещё раз?(да/нет)")
    if restart in ["да", "ДА", "Да"]:
        for row in field:
            for i in range(3):
                row[i] = "-"

        instruction()
        main(f)

    else:
        print("До встречи!")


main(field)
