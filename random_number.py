import random

random_number = random.randint(1,10)

while True:

    guess = int(input('Guess a number : '))

    if guess == random_number:
        print('You got it right! It is {}'.format(random_number))
        break
    else:
        print('Guess again!')
