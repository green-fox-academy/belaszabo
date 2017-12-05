try:
    file_name = "my-file.txt"
    f = open(file_name, "w")
    f.write("Bela")
    f.close()
except:
    print("Unable to write file:",file_name)