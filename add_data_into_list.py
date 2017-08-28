          // How to make python collect data and list data //

to_do_list = []                             // Add an empty list variable //

print('What should you do today?')          // Tells the user what to do //
print('Enter \'DONE\' when you are done.')  // Tells the user the EXIT command //

while True:                                 // True means it will loop forever until a 'break' is present //
    new_list = input(' > ')

    if new_list == 'DONE':                  // Add a If condition when the users types the exit command, it will break the loop //
        break
    else:                                   // Else, the loop continues //
        to_do_list.append(new_list)         // x.append(y) where x is the variable and y is the new input //


print('Here is what to do today \n >')

for to_do in to_do_list:                    // for loop for whatever it is saved within the list and breaks when there are nothing left //
    print(to_do)
