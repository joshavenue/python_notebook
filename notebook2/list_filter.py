nums = [5,10,15,20,25,30]

ping = list(filter(lambda x:x % 10 == 0, nums))

print(ping)

## Filter is like map but it feels like it includes if condition