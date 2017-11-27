a = int(input())
b = a - 1
for i in range(1, a + a * 1, 2):
    print(' ' * b + '*' * i )
    b -= 1