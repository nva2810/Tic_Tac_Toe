def rules():
    while True:
        game_rules = input('''Do you want to learn the rules of the game?
    ("yes" or "no"): ''')
        if game_rules == 'yes':
            print('''\nPlayers take turns placing signs on the free squares 
of the field (one is always a cross, the other is always zero). 
The winner is the one who first lines up his signs in a row vertically,
horizontally or diagonally. 
The first move is made by the player who puts crosses.\n''')
            tic_tac_toe(0)
        elif game_rules == 'no':
            print('X goes first!\n')
            tic_tac_toe(0)
        else:
            print('Invalid data. Please try again!\n')


def restart():
    while True:
        play_again = input('''Do you want to play again? 
        ("yes" or "no"): ''')
        if play_again == 'yes':
            global user_input
            user_input = [' ' for _ in range(9)]
            tic_tac_toe(0)
        elif play_again == 'no':
            print('Okay. Goodbye!')
            print(input('\nPress Enter to finish...'))
            quit()
        else:
            print('Invalid data. Please try again!\n')


def area():
    global user_input
    print(f'''  -------------
3 | {' | '.join(user_input[0:3])} |
  -------------
2 | {' | '.join(user_input[3:6])} |
  -------------
1 | {' | '.join(user_input[6:9])} |
  -------------
    1   2   3''')


def winner():
    v = [user_input[0:3], user_input[3:6], user_input[6:9]]  # vertical
    h = [user_input[0:9:3], user_input[1:9:3], user_input[2:9:3]]  # horizontal
    d = [user_input[0:9:4], user_input[2:8:2]]  # diagonal
    win = [['X', 'X', 'X'], ['O', 'O', 'O']]
    if win[0] in v or win[0] in h or win[0] in d:
        print('\n||| X wins |||\n')
        restart()
    elif win[1] in v or win[1] in h or win[1] in d:
        print('\n||| O wins |||\n')
        restart()
    elif ' ' not in user_input:
        print('\n...Draw...\n')
        restart()


def tic_tac_toe(start):
    area()
    while True:
        n = input('\nEnter the coordinates: ').split()
        if ''.join(n).isdigit() and len(n) == 2:
            index = (int(n[0]) - 1) + (9 - (3 * int(n[1])))
            if -1 < index < 9:
                if user_input[index] == ' ':
                    if start % 2 == 0:
                        user_input[index] = 'X'
                        area()
                        winner()
                    else:
                        user_input[index] = 'O'
                        area()
                        winner()
                    start += 1
                else:
                    print('This cell is occupied! Choose another one!')
            else:
                print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter two numbers!')


user_input = [' ' for x in range(9)]
print('''-------------------
| TIC | TAC | TOE |
-------------------
  for two players
                v1.0 by NVA\n''')
rules()
