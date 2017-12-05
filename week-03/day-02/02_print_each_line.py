file_name = "my-file.txt"
try:
    f = open(file_name, "r")
    print(f.read())
    f.close()
except IOError:
    print("Unable to read file:", file_name)