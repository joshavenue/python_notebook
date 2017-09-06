def packer(**kwargs):
	print(kwargs)

def unpacker(first_name=None,last_name=None):

	if first_name and last_name:
		print(first_name,last_name)
	else:
		print('Anon.')


packer(name='John Kennedy',age=23,agent_code=None)
unpacker(**{'first_name': 'John', 'last_name': 23})
