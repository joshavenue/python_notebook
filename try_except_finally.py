try:
    x = int(input('Enter a number : '))
except ValueError:
    print('Value is not a number.')
finally:
    print('You did typed something.')       ## Execute no matter what
