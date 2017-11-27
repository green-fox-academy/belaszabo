# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was
a = int(input())
for i in range(1,a,2):
    print(' ' * (i-1) + '*' *i)