# Write your code here
from board import Board
from exceptions import PositionError, MoveError


def check_first_position(position_list, x_board, y_board):
    try:
        x, y = [int(item) for item in position_list]
    except ValueError and ValueError:
        raise PositionError
    else:
        if x > x_board or y > y_board or x < 1 or y < 1:
            raise PositionError


def check_move(move_list, x_board, y_board):
    try:
        check_first_position(move_list, x_board, y_board)
    except PositionError:
        raise MoveError
    else:
        x = int(move_list[0])
        y = int(move_list[1])
        if (x, y) not in play_board.possible_move:
            raise MoveError


def check_game_status(count):
    if len(play_board.visit) == play_board.cell:
        print('\nWhat a great tour! Congratulations!')
        return False
    elif len(play_board.possible_move) == 0:
        print('\nNo more possible moves!')
        print(f'Your knight visited {count} squares!')
        return False
    else:
        return True


def find_solution(game_board, x, y):
    game_board.move(x, y)
    if len(game_board.visit) == game_board.cell:
        return True
    if len(game_board.possible_move) == 0:
        return False

    for move in game_board.possible_move:
        x_next, y_next = move
        if find_solution(game_board, x_next, y_next):
            return True
        game_board.visit.remove(move)
    return False


# ------------------------- 1. Create the board ----------------------#
while True:
    try:
        x_size, y_size = [int(item) for item in input("Enter your board dimensions: > ").split(' ')]
    except ValueError and ValueError:
        print("Invalid dimensions!")
    else:
        if x_size < 1 or y_size < 1:
            print("Invalid dimensions!")
        else:
            break
board = Board(x_size, y_size)

# ------------------------- 2. Create Start Position ----------------------#
while True:
    position_input = input("Enter the knight's starting position: > ").split(' ')
    try:
        check_first_position(position_input, x_size, y_size)
    except PositionError:
        print("Invalid position!")
    else:
        break
x_start = int(position_input[0])
y_start = int(position_input[1])

# ------------------------- 3. User's choice ----------------------#
while True:
    choice = input('Do you want to try the puzzle? (y/n): ')
    if choice == 'n' or choice == 'y':
        break
    else:
        print('Invalid input!')

# ------------------------- 4. Game Set Up ----------------------#
have_solution = find_solution(board, x_start, y_start)
if have_solution:
    if choice == 'n':
        print("\nHere's the solution!")
        board.display_solution()
    else:
        play_board = Board(x_size, y_size)
        play_board.move(x_start, y_start)
        play_board.display_board()
        game_round_count = 1
        game_on = True
        while game_on:
            next_move = input("Enter your next move: > ").split(' ')
            try:
                check_move(next_move, x_size, y_size)
            except MoveError:
                print("Invalid move!", end=' ')
            else:
                x_start = int(next_move[0])
                y_start = int(next_move[1])
                play_board.move(x_start, y_start)
                play_board.display_board()
                game_round_count += 1

                game_on = check_game_status(game_round_count)
else:
    print('No solution exists!')

