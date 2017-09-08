def generate_multiples(m,n):
	count = 0
	while count < n:
		yield m * count
		count += 1

def main():
	for multi in generate_multiples(9,10):
		print(multi, end=" ")

if __name__ == '__main__':
	main()