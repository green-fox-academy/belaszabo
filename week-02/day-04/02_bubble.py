a_list = [2, 3, 5, 17]
increasing = True

def sorter(list_of_numbers):
    for numbers in list_of_numbers:
        for i in range(0,len(list_of_numbers) - 1):
            if increasing == True:
                if list_of_numbers[i] > list_of_numbers[i+1]:
                    list_of_numbers[i], list_of_numbers[i+1] = list_of_numbers[i+1], list_of_numbers[i]
            else:
                if list_of_numbers[i] < list_of_numbers[i+1]:
                    list_of_numbers[i], list_of_numbers[i+1] = list_of_numbers[i+1], list_of_numbers[i]
    return list_of_numbers

print(sorter(a_list))