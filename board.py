MOVE_RULE = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


class Board:
    def __init__(self, x_, y_):
        self.X = x_
        self.Y = y_
        self.knight_x = 0
        self.knight_y = 0
        self.cell = len(str(x_ * y_))
        self.line = ' ' + '-' * ((self.cell + 1) * x_ + 3)
        self.placeholder = '_' * self.cell

    def x_format(self, num):
        output = ' ' * (self.cell - len(str(num)) + 1) + str(num + 1)
        return output

    def y_format(self, num):
        output = ' ' * (len(str(self.Y)) - len(str(num))) + str(num)
        return output

    def format(self, symbol):
        output = ' ' * (self.cell - 1) + symbol
        return output

    def display_next_step(self, x, y, next_step):
        for x_to, y_to in next_step:
            if x + 1 == x_to and y == y_to:
                num = len(self.find_possible_move(x_to, y_to)) - 1
                print(self.format(str(num)), end=' ')
                return True
        return False

    def display_board(self, next_step):
        print(self.line)
        for y in range(self.Y, 0, -1):
            print(f'{self.y_format(y)}|', end=' ')
            for x in range(self.X):
                if self.display_next_step(x, y, next_step):
                    continue
                if x + 1 == self.knight_x and y == self.knight_y:
                    print(self.format('X'), end=' ')
                else:
                    print(self.placeholder, end=' ')
            print('|')
        print(self.line)
        print('  ', end='')
        for x in range(self.X):
            print(self.x_format(x), end='')
        print(' ')

    def move(self, x_position, y_position):
        self.knight_x = x_position
        self.knight_y = y_position
        next_step = self.find_possible_move(x_position, y_position)
        self.display_board(next_step)

    def is_possible_move(self, x, y):
        if 0 < x <= self.X and 0 < y <= self.Y:
            return True
        else:
            return False

    def find_possible_move(self, x_pos, y_pos):
        possible_move = []
        for x, y in MOVE_RULE:
            x_possible = x_pos + x
            y_possible = y_pos + y
            if self.is_possible_move(x_possible, y_possible):
                possible_move.append((x_possible, y_possible))
        return possible_move


