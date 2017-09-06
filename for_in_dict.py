class_duration = {'English': 250,'Japanese': 300, 'Chinese': 350}

for key in class_duration.keys():
    print(key)                            // Prints out the Key only
    
for value in class_duration.values():
    print(value)                          // Prints out the value only
    
for item in class_duration.items():
    print(item)                           // Prints out the key + value
