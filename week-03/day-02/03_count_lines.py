def count_lines(string):
    try:
        f = open(string, "r")
        lines = f.readlines()
        f.close()
        return len(lines)
    except:
        return 0

print(count_lines("hello.txt"))