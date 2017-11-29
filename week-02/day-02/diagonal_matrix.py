# - Create (dynamically) a two dimensional list
#   with the following matrix. Use a loop!
#
#   1 0 0 0
#   0 1 0 0
#   0 0 1 0
#   0 0 0 1
#
# - Print this two dimensional list to the output

#for i in range(4):
#    a = [0]
#    a[i] = 1
#    print(a)
a = []
b = []
size = 4
 
for i in range(size):
    b = []
    for j in range(size):
        if i == j: 
            b.append('1')
        else:
            b.append('0')
    a.append(b)

for i in range(size):
     print(a[i])