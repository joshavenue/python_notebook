pairs = {1: "apple",
  "orange": [2, 3, 4], 
  True: False, 
  None: "True",
}

print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))

## .get(x) gets something from the dictionary, if it cant get the file, it will return something like none '
