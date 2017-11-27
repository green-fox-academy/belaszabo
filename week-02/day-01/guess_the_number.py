# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8
a = int(input('Write a number: '))
b = int(input('Guess: '))
while a != b:
    if a > b:    
        print('The stored number is higher')
        b = int(input('Guess again: '))
    elif a < b:
        print('The stored number is lower')
        b = int(input('Guess again: '))
    else:
        b = int(input('Guess again: '))
print('You found the number',a)