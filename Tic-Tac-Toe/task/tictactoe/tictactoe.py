class TicTacToe:

    def __init__(self, dimension):
        self.dim = dimension
        # ' ' means free space; 'X' means player 1; 'O' means player 2
        self.state = [[' ' for _ in range(self.dim)] for __ in range(self.dim)]

    def show(self):
        print('-' * (3 + 3 * (self.dim - 1)))
        for i in range(self.dim):
            print("| ", end='')
            for j in range(self.dim):
                print(self.state[i][j] + ' ', end='')
            print('|')
        print('-' * (3 + 3 * (self.dim - 1)))

    def make_move(self, cur_player):
        good_coords = False
        while not good_coords:
            pos_x, pos_y = input('Enter the coordinates:').split()
            if not pos_x.isdecimal() or not pos_y.isdecimal():
                print('You should enter numbers!')
                continue
            pos_x = int(pos_x)
            pos_y = int(pos_y)
            if not (1 <= pos_x <= self.dim) or not (1 <= pos_y <= self.dim):
                print(f'Coordinates should be from 1 to {self.dim}!')
                continue
            if self.state[self.dim - pos_y][pos_x - 1] != " ":
                print('This cell is occupied! Choose another one!')
                continue
            self.state[self.dim - pos_y][pos_x - 1] = cur_player
            good_coords = True

    def check(self):
        num_x = 0
        num_y = 0
        num_empty = 0
        for i in range(self.dim):
            for j in range(self.dim):
                if self.state[i][j] == 'X':
                    num_x += 1
                elif self.state[i][j] == 'O':
                    num_y += 1
                elif self.state[i][j] == ' ':
                    num_empty += 1
        if abs(num_x - num_y) >= 2:
            return True, 'Impossible'
        num_row_x = 0
        num_row_o = 0
        num_col_x = 0
        num_col_o = 0
        for i in range(self.dim):
            if all((True if p == 'X' else False for p in self.state[i])):
                num_row_x += 1
            elif all((True if p == 'O' else False for p in self.state[i])):
                num_row_o += 1
        for j in range(self.dim):
            column = []
            for i in range(self.dim):
                column.append(self.state[i][j])
            if all((True if p == 'X' else False for p in column)):
                num_col_x += 1
            elif all((True if p == 'O' else False for p in column)):
                num_col_o += 1
        if num_row_x >= 1 and num_row_o >= 1:
            return True, 'Impossible'
        if num_col_x >= 1 and num_col_o >= 1:
            return True, 'Impossible'
        if num_row_x == 1 or num_col_x == 1:
            return True, "X wins"
        if num_row_o == 1 or num_col_o == 1:
            return True, "O wins"
        main_diagonal = [self.state[i][i] for i in range(self.dim)]
        if all((True if p == 'X' else False for p in main_diagonal)):
            return True, 'X wins'
        if all((True if p == 'O' else False for p in main_diagonal)):
            return True, 'O wins'
        dop_diagonal = [self.state[i][self.dim - 1 - i] for i in range(self.dim)]
        if all((True if p == 'X' else False for p in dop_diagonal)):
            return True, 'X wins'
        if all((True if p == 'O' else False for p in dop_diagonal)):
            return True, 'O wins'
        if num_empty >= 1:
            return False, 'Game not finished'
        return True, "Draw"


game = TicTacToe(3)
game.show()
player = "X"
result = False
while not result:
    game.make_move(player)
    game.show()
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    result = game.check()[0]
print(game.check()[1])
