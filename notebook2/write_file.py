file = open('hi.txt', 'w')
file.write('\nLife is such nothing but a faint. ')    ## It will overwrite everything within the txt file.
file.close()

file = open('hi.txt', 'r')
print(file.read())
file.close()
