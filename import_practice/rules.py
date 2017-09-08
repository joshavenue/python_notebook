from prime_number_check import is_prime

x = int(input('Enter a number : '))

if is_prime(x):
	print('It is a prime')
else:
	print('It is not a prime')