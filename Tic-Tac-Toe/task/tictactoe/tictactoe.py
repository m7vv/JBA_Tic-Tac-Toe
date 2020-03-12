def show(state):
    for i in range(len(state)):
        for j in state[i]:
            if j == 1:
                print('X', end=' ')
            else:
                print('O', end=' ')
        print()


stateGame = [
    (1, 0, 1),
    (0, 0, 1),
    (1, 0, 1)
]

show(stateGame)
