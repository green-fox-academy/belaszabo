def mult_lines(path, word, number):
    try:
        file_name = path
        f = open(file_name, "w")
        for _ in range(number):
            f.write(str(word)+"\n")
        f.close()
    except:
        print("Unable to write:",file_name)


mult_lines("test.txt", "apple", 5)