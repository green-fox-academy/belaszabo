# Write a recursive function that takes one parameter: n and counts down from n.

def countdown(n):
    if n == 0:
        return 0
    else:
        print (n)
        return countdown(n-1)

print(countdown(10))