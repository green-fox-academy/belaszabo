# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was
a = int(input())
b = a - 1
c = a * 2 -1
for i in range(1, a + a * 1, 2):
    print(' ' * b + '*' * i )
    b -= 1
for o in range(1, a + a * 1, 2):
    print(' ' * (o-2) + '*' * c )
    c -= 2