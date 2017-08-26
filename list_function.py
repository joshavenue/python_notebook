number = [1,2,3,4,5]

x = any_number OR string;

number.append(x) // Adds a new data into the list //
OR number.append([x]) // Adds a new list into the list //
print(number)

number.extend([x,x1,x2]) // Adds more than two data into the list, does not create a list //
print number

number.remove(x) // Remove a data within the list
OR number.remove([x]) // Removes a list within a list
print number
