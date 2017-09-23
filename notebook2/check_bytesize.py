msg = 'The world is a funny place to live.'
file = open('hi.txt', 'w')
amount_written = file.write(msg)
print(amount_written)
file.close()

## file.write(x) is the same as len(x) ##
