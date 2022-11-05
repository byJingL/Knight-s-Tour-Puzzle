MOVE_RULE = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]


class Board:
    def __init__(self, x_, y_):
        self.X = x_
        self.Y = y_
        self.current_x = None
        self.current_y = None
        self.cell = x_ * y_
        self.empty = len(str(x_ * y_))
        self.line = ' ' + '-' * ((self.empty + 1) * x_ + 3)
        self.placeholder = '_' * self.empty
        self.possible_move = []
        self.visit = []

    def x_format(self, num):
        output = ' ' * (self.empty - len(str(num)) + 1) + str(num + 1)
        return output

    def y_format(self, num):
        output = ' ' * (len(str(self.Y)) - len(str(num))) + str(num)
        return output

    def mark(self, symbol):
        output = ' ' * (self.empty - len(symbol)) + symbol
        print(output, end=' ')
        return output

    def mark_next_step(self, x, y, next_step):
        for x_to, y_to in next_step:
            if x + 1 == x_to and y == y_to:
                num = len(self.find_possible_move(x_to, y_to))
                self.mark(str(num))
                return True
        return False

    def mark_visited(self, x, y):
        for x_ed, y_ed in self.visit:
            if x + 1 == x_ed and y == y_ed:
                self.mark('*')
                return True
        return False

    def display_board(self):
        print(self.line)
        for y in range(self.Y, 0, -1):
            print(f'{self.y_format(y)}|', end=' ')
            for x in range(self.X):
                if x + 1 == self.current_x and y == self.current_y:
                    self.mark('X')
                elif self.mark_visited(x, y):
                    continue
                elif self.mark_next_step(x, y, self.possible_move):
                    continue
                else:
                    print(self.placeholder, end=' ')
            print('|')
        print(self.line)
        print('  ', end='')
        for x in range(self.X):
            print(self.x_format(x), end='')
        print(' ')

    def move(self, x_pos, y_pos):
        self.current_x = x_pos
        self.current_y = y_pos
        next_step = self.find_possible_move(x_pos, y_pos)
        self.possible_move = next_step
        self.visit.append((self.current_x, self.current_y))

    def is_possible_move(self, x, y):
        if 0 < x <= self.X and 0 < y <= self.Y and (x, y) != (self.current_x, self.current_y):
            for (x_ed, y_ed) in self.visit:
                if (x, y) == (x_ed, y_ed):
                    return False
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

    def display_solution(self):
        # print(self.visit)
        print(self.line)
        for y in range(self.Y, 0, -1):
            print(f'{self.y_format(y)}|', end=' ')
            for x in range(self.X):
                for i in range(len(self.visit)):
                    if (x + 1, y) == self.visit[i]:
                        self.mark(f'{i + 1}')
            print('|')
        print(self.line)
        print('  ', end='')
        for x in range(self.X):
            print(self.x_format(x), end='')
        print(' ')
