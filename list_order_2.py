def first_4(x):
    return x[:4]

def first_and_last_4(x):
    y = x[:4]                      // From index 0 till 4
    y = y + x[-4:]                // Add another from last index till the last 4 index
    return y

def reverse_even(x):
    return x[::2][::-1]             // You can actually do this
