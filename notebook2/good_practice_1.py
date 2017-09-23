try:
	file = open('hi.txt')
	print(file.read())
finally:
	file.close()
