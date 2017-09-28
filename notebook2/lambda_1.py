#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

print((lambda y: y*2 + 5) (5))

def linear(y):
	return y*2 + 5
print(linear(5))