import random

lives = 3
count = 0

print('*type either rock, paper, or scissors*')

while lives > 0:

    print(f"**You have {lives} lives, play wisely**")

    player1 = input('Make your move: ').lower()
    
    if player1 == "quit":
    	break
    
    rand_num = random.randint(0,2)

    if rand_num == 0:
        player2 = 'rock'
    elif rand_num == 1:
        player2 = 'scissors'
    elif rand_num == 2:
        player2 = 'paper'

    print("The computer played: ", player2)

    if player1 == 'rock':
        if player2 == 'scissors':
            print('You win!')
            count += 1
            print(count,' wins')
        if player2 == 'paper':
            print('Computer wins!')
            lives -= 1
            if lives < 1:
                play_again = input('Do you want to play again? (y/n) ')
                if play_again == 'y':
                    lives += 3
        if player2 == 'rock':
            print('Redo!')
    elif player1 == 'paper':
        if player2 == 'rock':
            print('You win!')
            count += 1
            print(count,' wins')
        if player2 == 'scissors':
            print('Computer wins!')
            lives -= 1
            if lives < 1:
                play_again = input('Do you want to play again? (y/n) ')
                if play_again == 'y':
                    lives += 3
        if player2 == 'paper':
            print('Redo!')
    elif player1 == 'scissors':
        if player2 == 'rock':
            print('Computer wins!')
            lives -= 1
            if lives < 1:
                play_again = input('Do you want to play again? (y/n) ')
                if play_again == 'y':
                    lives += 3
        if player2 == 'paper':
            print('You win!')
            count += 1
            print(count,' wins')
        if player2 == 'scissors':
            print('Redo!')

    else:
        print('You spelled something wrong...')

print('Hope you had some fun! Game over!')
