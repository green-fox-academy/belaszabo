def search_palindrome(string):
    strings = string.split()
    print(strings)
    palindromes = []
    for i in range(0,len(strings)):
        if len(strings[i]) % 2 == 0:
            if strings[i][:len(strings[i])/2+1] == strings[i][len(strings[i])/2:]:
                palindromes.append(strings[i])
    return palindromes

print(search_palindrome("hello ka racecar"))