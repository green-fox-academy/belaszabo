def strsearch(str1, str2):
    if str2 in str1:
        return str1.index(str2)
    else:
        return -1

print(strsearch("this is what I'm searching in", "searching"))