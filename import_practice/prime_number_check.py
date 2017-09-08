from math import sqrt

def is_prime(n):

	trial_factor = 2
	root = sqrt(n)

	while trial_factor <= root:
		if n & trial_factor == 0:
			return False
		trial_factor += 1

	return True
