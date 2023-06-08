def rules():
    while True:
        game_rules = input('''Хотите узнать правила игры?
    ("да" или "нет"): ''')
        if game_rules == 'да':
            print('''\nИгроки по очереди расставляют знаки на свободных
квадратах поля (один всегда крестик, другой всегда нолик).
Побеждает тот, кто первым выстроит свои знаки в ряд по вертикали,
горизонтали или диагонали.
Первый ход делает игрок, который ставит крестики.\n''')
            tic_tac_toe(0)
        elif game_rules == 'нет':
            print('X ходит первым!\n')
            tic_tac_toe(0)
        else:
            print('Неверные данные. Пожалуйста, попробуйте еще раз!\n')


def restart():
    while True:
        play_again = input('''Хотите сыграть снова? 
        ("да" или "нет"): ''')
        if play_again == 'да':
            global user_input
            user_input = [' ' for _ in range(9)]
            tic_tac_toe(0)
        elif play_again == 'нет':
            print('Хорошо. До свидания!')
            print(input('\nНажмите Enter, чтобы закончить...'))
            quit()
        else:
            print('Неверные данные. Пожалуйста, попробуйте еще раз!\n')


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
        print('\n||| X побеждает |||\n')
        restart()
    elif win[1] in v or win[1] in h or win[1] in d:
        print('\n||| O побеждает |||\n')
        restart()
    elif ' ' not in user_input:
        print('\n...Ничья...\n')
        restart()


def tic_tac_toe(start):
    area()
    while True:
        n = input('\nВведите координаты: ').split()
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
                    print('Эта ячейка занята! Выберите другую!')
            else:
                print('Координаты должны быть от 1 до 3!')
        else:
            print('Вы должны ввести две цифры!')


user_input = [' ' for x in range(9)]
print('''-------------------
| TIC | TAC | TOE |
-------------------
  для двух игроков
                v1.0 by NVA\n''')
rules()
