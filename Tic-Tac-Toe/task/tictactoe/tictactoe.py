def show(state_l):
    print('-' * 9)
    for i in range(3):
        print("| {} {} {} |".format(state_l[i][0], state_l[i][1], state_l[i][2]))
    print('-' * 9)


def state_str2list(str_input):
    """
    convert state of game from string to list of list
    """
    state = [[0 for _ in range(3)] for __ in range(3)]
    str_input = str_input.replace("_", " ")

    state[0][0] = str_input[0]
    state[0][1] = str_input[1]
    state[0][2] = str_input[2]
    state[1][0] = str_input[3]
    state[1][1] = str_input[4]
    state[1][2] = str_input[5]
    state[2][0] = str_input[6]
    state[2][1] = str_input[7]
    state[2][2] = str_input[8]
    return state


def check(state):
    num_x = 0
    num_y = 0
    num_empty = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == 'X':
                num_x += 1
            elif state[i][j] == 'O':
                num_y += 1
            elif state[i][j] == ' ':
                num_empty += 1
    if abs(num_x - num_y) >= 2:
        return True, 'Impossible'
    num_row_x = 0
    num_row_y = 0
    num_col_x = 0
    num_col_y = 0
    for i in range(3):
        if state[i][0] == state[i][1] == state[i][2] == 'X':
            num_row_x += 1
        elif state[i][0] == state[i][1] == state[i][2] == 'O':
            num_row_y += 1
        if state[0][i] == state[1][i] == state[2][i] == 'X':
            num_col_x += 1
        elif state[0][i] == state[1][i] == state[2][i] == 'O':
            num_col_y += 1
    if num_row_x >= 1 and num_row_y >= 1:
        return True, 'Impossible'
    if num_col_x >= 1 and num_col_y >= 1:
        return True, 'Impossible'
    if num_row_x == 1 or num_col_x == 1:
        return True, "X wins"
    if num_row_y == 1 or num_col_y == 1:
        return True, "O wins"
    if state[0][0] == state[1][1] == state[2][2] == 'X':
        return True, 'X wins'
    if state[0][0] == state[1][1] == state[2][2] == 'O':
        return True, 'O wins'
    if state[0][2] == state[1][1] == state[2][0] == 'X':
        return True, 'X wins'
    if state[0][2] == state[1][1] == state[2][0] == 'O':
        return True, 'O wins'
    if num_empty >= 1:
        return False, 'Game not finished'
    return True, "Draw"


def make_move(state, cur_player):
    good_coords = False
    while not good_coords:
        pos_x, pos_y = input('Enter the coordinates:').split()
        if not pos_x.isdecimal() or not pos_y.isdecimal():
            print('You should enter numbers!')
            continue
        pos_x = int(pos_x)
        pos_y = int(pos_y)
        if not (1 <= pos_x <= 3) or not (1 <= pos_y <= 3):
            print('Coordinates should be from 1 to 3!')
            continue

        if state[3 - pos_y][pos_x - 1] != " ":
            print('This cell is occupied! Choose another one!')
            continue
        state[3 - pos_y][pos_x - 1] = cur_player
        good_coords = True


state_game = state_str2list("_" * 9)
show(state_game)
player = "X"
result = False
while not result:
    make_move(state_game, player)
    show(state_game)
    if player == 'X':
        player = 'O'
    else:
        player = 'X'
    result = check(state_game)[0]
print(check(state_game)[1])
