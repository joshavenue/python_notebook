def gen():
	yield 3				# Like return but one by one
	yield 'wow'
	yield -1
	yield 1.2

x = gen()

print(next(x))			# Use next() function to go one by one
print(next(x))

print(next(x))
print(next(x))