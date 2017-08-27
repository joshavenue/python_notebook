// List function //
// For example //
name = 'John, Lewis, Clark'
list(name) // List all the strings in an list function //

print(list(name)) 

// Split method //

name.split() // Separates all strings into its own list //

// Join method //

', '.join(name) // Join new things into a list //

You can join things like this way -->

'Hi, my friend\'s name are '.join(name)

OR

'My friend\'s name are {}.'.format(''.join(name))
