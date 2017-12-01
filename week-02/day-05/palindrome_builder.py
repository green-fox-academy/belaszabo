def create_palindrome():
    word = input('Write any string: ')
    palindrome = word + word[::-1]
    return palindrome

print(create_palindrome())