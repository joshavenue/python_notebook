# EXAMPLES
# squared(5) would return 25
# squared("2") would return 4
# squared("tim") would return "timtimtim"

def squared(num):
    try:
        x = int(num) ** 2
        return x
    except ValueError:
        return num * len(num)
