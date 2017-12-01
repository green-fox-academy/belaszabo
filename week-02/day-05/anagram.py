def anagram(str1, str2):
    str1_list = []
    str2_list = []
    for i in range(0,len(str1)):
        str1_list.append(str1[i])
    for i in range(0,len(str2)):
        str2_list.append(str2[i])
    if str1_list.sort == str2_list.sort:
        return True
    else:
        return False

print(anagram("anna", "annn"))