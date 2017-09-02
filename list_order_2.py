def first_4(iterable):
    return iterable[:4]

def first_and_last_4(iterable):
    list1 = iterable[:4]                  // From index 0 till 4
    list1 = list1 + iterable[-4:]         // Add another from last index till the last 4 index
    return list1
