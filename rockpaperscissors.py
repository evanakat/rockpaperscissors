import random

games = [1 , 3, 4 ,5, 6, 7, 8, 9, 10]

for game in games:

    player1 = input('Player 1, make your move: ').lower()

    rand_num = random.randint(0,2)

    if rand_num == 0:
        player2 = 'rock'
    elif rand_num == 1:
        player2 = 'scissors'
    elif rand_num == 2:
        player2 = 'paper'

    print("The computer played:", player2)

    if player1 == 'rock':
        if player2 == 'scissors':
            print('Player 1 wins!')
        if player2 == 'paper':
            print('Player 2 wins!')
        if player2 == 'rock':
            print('Redo!')
    elif player1 == 'paper':
        if player2 == 'rock':
            print('Player 1 wins')
        if player2 == 'scissors':
            print('Player 2 wins!')
        if player2 == 'paper':
            print('Redo!')
    elif player1 == 'scissors':
        if player2 == 'rock':
            print('Player 2 wins!')
        if player2 == 'paper':
            print('Player 1 wins!')
        if player2 == 'scissors':
            print('Redo!')
    else:
        print('You spelled something wrong...')
print('Hope you had some fun! Game over!')
