def anagram(str1, str2):
    str1_list = []
    str2_list = []
    for i in range(0,len(str1)):
        str1_list.append(str1[i])
    for i in range(0,len(str2)):
        str2_list.append(str2[i])
    a = 0
    b = 0
    for i in range(0,len(str1_list)):
        if str1_list[i] == " ":
            a += 1
    for i in range(0,len(str1_list)):
        if str2_list[i] == " ":
            b += 1
    if b != 0:
        b2 = " " * b
        b2 = b2.split()
        str1_list. append(b2)
    if a != 0:
        a2 = " " * a
        a2 = a2.split()
        str2_list.append(a2)
    if sorted(str1_list) == sorted(str2_list):
        return True
    else:
        return False

print(anagram("anna", "an   na"))