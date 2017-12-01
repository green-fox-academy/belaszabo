def anagram(str1, str2):
    str1_list = []
    str2_list = []
    for i in range(0,len(str1)):
        str1_list.append(str1[i])
    for i in range(0,len(str2)):
        str2_list.append(str2[i])
    tmp1 = False
    tmp2= False
    if len(str1) == len(str2):
        for i in str1_list:
            if i in str2_list:
                tmp1 = True
        for i in str2_list:
            if i in str1_list:
                tmp2 = True
        return True if tmp1 == True and tmp2 == True else False
print(anagram("gyomorrontas", "toronymorgas"))