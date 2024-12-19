board_size = 3
board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def draw_board():
    """ Выводим игровое поле """
    print("_" * 4 * board_size)
    for i in range(board_size):
        print((" " * 3 + "|")*3)
        print('', board[i*3], "|", board[1 + i*3], "|", board[2 + i*3], "|")
        print(("_" * 3 + "|")*3)
    pass

def game_step(index, char):
    """ Делаем ход """
    if (index > 9 or index < 1 or board[index-1] in ("X", "O")):
        return False
    board[index-1] = char
    return True

def check_win():
    """Проверка на победу"""
    win = False
    result_win = (
        (0,1,2), (3,4,5), (6,7,8),   #Горизонтальные линии
        (0,3,6), (1,4,7), (2,5,8),   #Вертикальные линии
        (0,4,8), (2,4,6)             #Диагональные линии
    )
    for pos in result_win:
        if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]] ):
            win = board[pos[0]]
    return win

def start():
    player = 'X'
    step = 1
    draw_board()
    while (step < 10) and (check_win() == False):
        index = input("Ход игрока " + player + ". Введите номер поля(0 - выход): ")
        if (index == "0"):
            break
        if (game_step(int(index), player)):
            print("Ход выполнен")

            if (player == 'X'):
                player = 'O'
            else:
                player = 'X'

            draw_board()
            step += 1
        else:
            print("Неверно! Повторите ход")

    if (step == 10):
        print("Ничья! Игра окончена.")
    else:
        print("Победитель " + check_win())

start()