try:                                            // Tries to run this block of code //
    number = int(input('Enter a number'))
except ValueError:                              // If it captures input that is not an integer data //
    print('Not a number.')
else:                                           // If the condition is right, it will run it //
    print(' - ' * number)
