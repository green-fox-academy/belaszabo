# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.
def adder(n):
    if n == 1:
        return 1
    else:
        return n + adder(n-1)

print(adder(5))