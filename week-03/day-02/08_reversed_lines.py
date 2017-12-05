def decrypt(file_name):
    f = open(file_name, "r")
    content = f.readlines()
    f.close()
    new_content = []
    for lines in content:
        new_content.append(lines[::-1])
    file_name2 = "corrected.txt"
    string = ''.join(str(i) for i in new_content)
    f2 = open(file_name2, "w")
    f2.write(string)
    f2.close()

decrypt("reversed_lines.txt")