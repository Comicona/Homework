print('-' * 10 + ' Tic-tac-toe for two players ' + '-' * 10)

new_game = True

while new_game:

    board = list(range(1,10))
    counter = 0
    win_check = False
    win = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

    while not win_check:

        print('-' * 13)
        for i in range(3):
            print('|', board[0 + i*3], '|', board[1 + i*3], '|', board[2 + i*3], '|')
            print('-' * 13)

        if counter % 2 == 0:
            player_symbol = "X"
        else:
            player_symbol = "O"

        check = False

        while not check:

            player_choice = int(input('Куда ставим ' + player_symbol + '? '))
            if player_choice >= 1 and player_choice <= 9:
                if(str(board[player_choice-1]) not in "XO"):
                    board[player_choice-1] = player_symbol
                    check = True
                else:
                    print("Эта клетка уже занята!")
            else:
                print("Некорректный ввод. Введите число от 1 до 9.")

        counter += 1

        if counter > 4:
            for each in win:
                if board[each[0]] == board[each[1]] == board[each[2]]:
                    win_check = True
                else:
                    win_check = False
            
                if win_check:
                    print(player_symbol, "выиграл!")
                    game = input('Начать новую игру? ')
                    if game == 'Да' or game == 'да':
                        new_game = True
                    else:
                        new_game = False
                    break

        if counter == 9:
            print("Ничья!")
            game = input('Начать новую игру? ')
            if game == 'Да' or game == 'да':
                new_game = True
            else:
                new_game = False
            break
