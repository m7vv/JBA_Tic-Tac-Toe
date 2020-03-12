def show(state):
    print('-' * 9)
    for i in range(3):
        print("| {} {} {} |".format(state[0 + 3 * i], state[1 + 3 * i], state[2 + 3 * i]))
    print('-' * 9)


stateGame = input('Enter cells:')
show(stateGame)
