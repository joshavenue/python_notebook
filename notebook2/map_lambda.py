def fiveex(x):
	return x**x

nums = [1,2,3,5,7,11,13,17]

results = list(map(fiveex,nums))

print(results)

## The function map takes a function and an 
## iterable as arguments, and returns a new iterable 
## with the function applied to each argument. 

result = list(map(lambda x:x**x,nums))
print(result)

## Works for lambda style as well