file = open('hi.txt','r')

print('\n')

for line in file:
	print(line, end='')

print('\n')

file.close()
