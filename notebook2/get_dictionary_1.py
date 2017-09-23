fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))

## get(4,0) is 3 because as you can see, 4:3, in the key 4, you can 3. 
## Since there is not key 7, this will just equivalent to 5.
## 3 + 5 = 8

## output is 8
