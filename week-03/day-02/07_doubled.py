def decrypt(file_name):
    f = open(file_name, "r")
    content = f.read()
    f.close()
    content_simple = content[::2]
    file_name2 = "corrected.txt"
    f2 = open(file_name2, "w")
    f2.write(content_simple)
    f2.close()

decrypt("duplicated_chars.txt")