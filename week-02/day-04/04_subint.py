list_of_numbers = [1, 11, 34, 52, 61]
number = 1

def number_finder(list_of_numbers, number):
    new_list = []
    for numbers in list_of_numbers:
        new_list.append(str(numbers))
    for i in range(len(list_of_numbers)):
        if str(number) in new_list[i]:
            print (new_list.index(i))

number_finder(list_of_numbers, number)