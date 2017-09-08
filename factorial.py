def factorial(n):
    product = 1
    while n:                # Do not use while True to prevent poor optimization
        product *= n
        n -= 1
    return product

def main():
    print(" 0! = {}".format(factorial(0)))
    print(" 1! = {}".format(factorial(1)))
    print(" 2! = {}".format(factorial(2)))
    print(" 3! = {}".format(factorial(3)))

main()