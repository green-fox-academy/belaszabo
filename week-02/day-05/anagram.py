def anagram(str1, str2):
    # str1_list = []
    # str2_list = []
    # str1 = str1.split()
    # str2 = str2.split()
    str1 = "".join([sorted(str1)]).split()
    str2 = "".join([sorted(str2)]).split()
    # for i in range(0,len(str1)):
    #     str1_list.append(str1[i])
    # for i in range(0,len(str2)):
    #     str2_list.append(str2[i])
    # a = (len(str1_list))
    # b = (len(str2_list))
    # for i in range(0,a):
    #     if str1_list[i] == " ":
    #         del str1_list[i]
    #         a -= 2
    # for i in range(0,b):
    #     if str2_list[i] == " ":
    #         del str2_list[i]
    #         b -= 2
    # str1_list = str1_list.sort
    # str2_list = str2_list.sort
    # for i in range(0,len(str1_list)):
    #     if str1_list[i] == " ":
    #         str1_list = str1_list[i+1:]
    # for i in range(0,len(str2_list)):
    #     if str2_list[i] == " ":
    #         str2_list = str2_list[i+1:]
    # if str1_list.sort == str2_list.sort:
    #     return True
    # else:
    #     return False

    if str1 == str2:
        return True
    else:
        return False

print(anagram("anna", "an na"))