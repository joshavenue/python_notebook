import random

def game():

    random_number = random.randint(1,10)
    guess_time = []

    while len(guess_time) < 5:
        try:
            guess = int(input('Guess a number : '))
        except ValueError:
            print('{} is not a number'.format(guess))
        else:

            if guess == random_number:
                print('You got it right! It is {}'.format(random_number))
                break
            elif guess < random_number:
                print('My number is higher, try again.')
            else:
                print('Guess again, it is lower this time1!')
            guess_time.append(guess)
    else:
        print('You lost, the number was {}'.format(random_number))

    play_again = input('Do you want to play again? Y/N')

    if play_again.lower() != 'n':
        game()
    else:
        print('bye bye!')

game()
