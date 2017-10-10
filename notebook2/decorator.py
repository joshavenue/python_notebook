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

##---------------------------##

def p_t(foo):
	def thang():	
		print('bye')
		foo()
		print('mao')
	return thang

def stuff():
	print('bing') 

x = p_t(stuff)
x()
