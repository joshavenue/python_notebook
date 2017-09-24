nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
   print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
   print("At least one is even")

for v in enumerate(nums):
   print(v)

## all = take all iterable and check, say you wanna check 5 item in the list and make sure all is true, use all
## any = take some of the iterable and check, say you wanna check if one of the 5 item in the list is true, use any

## For example

a = [1,2,3,4,5,8,9,10]

if any([i < 3 for i in a]):
	print('bing')

if all([len(a) == 8 for i in a]):
	print('good')
else:
	print('not good')
