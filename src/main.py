import random
from time import sleep

from constants import BoardPosition, BoardDisplay, BoardGrid, InfoParameters


def get_line(position):
    global position_a, position_b, position_c
    position *= 2
    board_position = BoardPosition.BOARD.value

    position_a = int(board_position[position + 0])
    position_b = int(board_position[position + 1])
    position_c = int(board_position[position + 2])
    return board[position_a] + board[position_b] + board[position_c]


def ai_plays():
    for x in (2, 18):
        for position in range(8):
            if get_line(position) == x:
                position = get_position()

                board[position] = 1
                print(InfoParameters.PARAMS_SHOW_RESULT.value %
                      (BoardDisplay.BLUE.value, 'AI chose the position: ', (position + 1), BoardDisplay.RST.value))
                sleep(2)
                return

    while True:
        position = random.randint(0, 8)
        if board[position] == empty:
            board[position] = 1
            break

    print(InfoParameters.PARAMS_SHOW_RESULT.value %
          (BoardDisplay.BLUE.value, 'AI chose the position: ', (position + 1), BoardDisplay.RST.value))
    sleep(2)


def user_plays():
    while True:
        user_choice = input(
            InfoParameters.PARAMS.value % (BoardDisplay.GREEN.value, 'User chose the position: ', BoardDisplay.RST.value))

        if user_choice in ('q', 'Q', '0'):
            print('Game aborted...')
            exit(0)

        try:
            position = int(user_choice) - 1

            if board[position] != empty:
                print('Position already occupied')

            else:
                print(board[position])
                board[position] = 9
                print(board[position])
                break
        except KeyboardInterrupt:
            pass


def get_position():
    if board[position_a] == empty:
        return position_a

    elif board[position_b] == empty:
        return position_b

    else:
        return position_c


def show_board():
    global draw, ai_player, user_player
    mk = []
    for i, v in enumerate(board):
        if v == 0:
            mk.append(InfoParameters.PARAMS.value % (BoardDisplay.YELLOW.value, str(i + 1), BoardDisplay.RST.value))
        elif v == 1:
            mk.append(InfoParameters.PARAMS.value % (BoardDisplay.BLUE.value, 'O', BoardDisplay.RST.value))
        else:
            mk.append(InfoParameters.PARAMS.value % (BoardDisplay.GREEN.value, 'X', BoardDisplay.RST.value))

    show_results(mk)


def show_results(mk):
    print_results(BoardDisplay.WHITE.value, "Draws = ", draw)
    print_results(BoardDisplay.BLUE.value, 'AI   = ', ai_player)
    print_results(BoardDisplay.GREEN.value, 'User = ', user_player)

    print()
    print(BoardGrid.GRID.value % tuple(mk[0:3]))
    print(BoardGrid.SEPARATOR.value)
    print(BoardGrid.GRID.value % tuple(mk[3:6]))
    print(BoardGrid.SEPARATOR.value)
    print(BoardGrid.GRID.value % tuple(mk[6:9]))
    print()


def print_results(color, text, value):
    print(InfoParameters.PARAMS_SHOW_RESULT.value % (color, text, value, BoardDisplay.RST.value))


def verify_results():
    global draw, ai_player, user_player

    for position in range(8):
        if get_line(position) == 3:
            print(InfoParameters.PARAMS.value % (BoardDisplay.BLUE.value, 'AI Wins', BoardDisplay.RST.value))
            ai_player += 1
            sleep(2)
            return True

        elif get_line(position) == 27:
            print(InfoParameters.PARAMS.value % (BoardDisplay.GREEN.value, 'User Wins', BoardDisplay.RST.value))
            user_player += 1
            sleep(2)
            return True

    if empty not in board:
        print('Draw... :(')
        draw += 1
        sleep(2)
        return True

    return False


if __name__ == '__main__':
    draw = 0
    ai_player = 0
    user_player = 0
    empty = 0

    while True:
        board = [empty] * 9

        turn_control = random.choice([True, False])

        show_board()
        while True:

            turn_control = not turn_control

            if turn_control:
                ai_plays()
            else:
                user_plays()

            show_board()

            if verify_results():
                break

        key = input('Play again? (S/N)')
        if key not in ('S', 's'):
            break

    print('\nEnd Game')
