def unique(numbers_list):
    new_list = []
    for numbers in numbers_list:
        if numbers not in new_list:
            new_list.append(numbers)
    return new_list

list_of_numbers = [1, 11, 34, 11, 52, 61, 1, 34]

print (unique(list_of_numbers))