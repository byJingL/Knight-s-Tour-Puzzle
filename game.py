# Write your code here
from board import Board


class PositionError(Exception):
    pass


class DimensionError(Exception):
    pass


def check_board(board_list):
    if not len(board_list) == 2:
        raise DimensionError
    else:
        for letter in board_list:
            try:
                int(letter)
            except ValueError:
                raise DimensionError
            else:
                if int(letter) < 0:
                    raise DimensionError


def check_position(position_list, x_board, y_board):
    if not len(position_list) == 2:
        raise PositionError
    else:
        for letter in position_list:
            try:
                int(letter)
            except ValueError:
                raise PositionError
            else:
                x = int(position_list[0])
                y = int(position_list[1])
                if x > x_board or y > y_board or x < 1 or y < 1:
                    raise PositionError


# ------------------------- Create the board ----------------------#
board_size = input("Enter your board dimensions: > ").split(' ')
try:
    check_board(board_size)
except DimensionError:
    print("Invalid dimensions!")
# ------------------------- Create Start Position ----------------------#
else:
    while True:
        x_size = int(board_size[0])
        y_size = int(board_size[1])
        position_input = input("Enter the knight's starting position: > ").split(' ')
        try:
            check_position(position_input, x_size, y_size)
        except PositionError:
            print("Invalid position!")
        else:
            break
# ------------------------- Game Set Up ----------------------#
    new_game = Board(x_size, y_size)

    x_index = int(position_input[0])
    y_index = int(position_input[1])

    print('Here are the possible moves:')
    new_game.move(x_index, y_index)


