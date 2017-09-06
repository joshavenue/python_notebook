# | or .union(*others) - all of the items from all of the sets
# & or .intersection(*others) - all of the common items between all of the sets
# - or .difference(*others) - all of the items in the first set that are not in the other sets
# ^ or .symmetric_difference(other) - all of the items that are not shared by the two sets

set1 = {1,3,5,7,9,11,13,15,17,19}
set2 = {1,2,5,7,11,13,17,19}

set1.union(set2)                # {1,2,3,5,7,9,11,13,15,17,19} , It combines everything without overlapping

set1.intersection(set2)         # {1,5,7,11,13,17,19} , find the similar items between two sets

set1.difference(set2)           # {9,3,15} , compare the difference between set1 and set2

set1.symmetric_difference(set2) # {2,3,9,15}, find numbers that are not shared between the two lists. Better version of .difference()
