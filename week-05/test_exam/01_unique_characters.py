# Create a function called `unique_characters` that takes a string as parameter
# and returns a list with the unique letters of the given string
# Create basic unit tests for it with at least 3 different test cases
# print(unique_characters("anagram"))
# Should print out:
# ["n", "g", "r", "m"]

def unique_characters(string):
    original_string = []
    multiple_occurence_string = []
    unique_string = []

    for char in string:
        original_string.append(char)
    for char in original_string:
        if char in unique_string:
            unique_string.remove(char)
            multiple_occurence_string.append(char)
        if char not in unique_string and char not in multiple_occurence_string:
            unique_string.append(char)
    return unique_string

print(unique_characters("anagram"))