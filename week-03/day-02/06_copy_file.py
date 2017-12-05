def copy(c_from, c_to):
    try:
        file_from = c_from
        file_to = c_to
        f = open(file_from, "r")
        content = f.read()
        f.close()
        f2 = open(file_to, "w")
        f2.write(content)
        f2.close()
        return True
    except:
        return False

copy("test1.txt", "test2.txt")