list_of_numbers = [1, 11, 34, 52, 61]
number = 1 
#new_list = []

def number_finder(list_of_numbers, number):
    new_list = []
    #for numbers in list_of_numbers:
    #    new_list.append(str(numbers))
    if number in new_list:
        return new_list.index(number) - 2 * new_list.index(number)

print(number_finder(list_of_numbers, number))