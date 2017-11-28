# - Create a function called `factorio`
#   that returns it's input's factorial
def factorio(number):
    total = 1
    for i in range(1,number+1):
        total *= i
    return total

print(factorio(7))