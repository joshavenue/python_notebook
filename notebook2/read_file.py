file = open('hi.txt','r')
cont = file.read()
print(cont)
file.close()
##--------------##
file = open('hi.txt','r')
print(file.read(16))        ## This determines the number of bytes that should be read.
print(file.read(4))         ## You can make more calls to read on the same file object to read more of the file byte by byte.
print(file.read(4))         ## ## With no argument, read returns the rest of the file.
print(file.read())
file.close()
