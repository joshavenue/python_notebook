def decor(func):
	def wrap():
		print('===')
		func()
		print('===')
	return wrap

def print_text():
	print('Text')

decorated = decor(print_text)
decorated()
