def num(*nums):             // One * takes in any number of single data type, in this case : Int
    sum = 0
    for x in nums:
        sum += x
    return sum
    
sum(22,33,44,55,66)         // You can type as many numbers as you wish


def whatever(**kwargs):     // Double ** take more than just a type of data, in this case, there is Str and Int
    print(first_name)
    print(last_name)
    print(age)
    
whatever('first_name': 'John', 'last_name': 'Lee', 'age': 22)     // Create a dictionary


    
