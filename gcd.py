def gcd(m,n):
	if n == 0:
		return m
	else:
		return gcd(n, m % n)

def iterative_gcd(num1, num2):

	min = num1 if num1 < num2 else num2

	largest_factor = 1
	for i in range(1, min + 1):
		if num1 % i == 0 and num2 % i == 0:
			largest_factor = i
	return largest_factor

def main():

	for num1 in range(1, 101):
		for num2 in range (1, 101):
			print("GCD of {} and {} is {}.".format(num1,num2,gcd(num1,num2)))

main()