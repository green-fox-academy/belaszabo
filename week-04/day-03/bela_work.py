class Apple(object):

    def get_apple(self):
        return "apple"


    def summa(self, list_of_integers):
        total = 0
        if list_of_integers != []:
            for number in list_of_integers:
                if type(number) == int:
                    total += number
                else:
                    return "Enter a list of numbers"
        else:
            total = 0
        return total


    def anagram(self, string1, string2):
        list_of_string1 = []
        list_of_string2 = []
        for letter in string1:
            list_of_string1.append(letter)
        for letter in string2:
            list_of_string2.append(letter)
        list_of_string1.sort()
        list_of_string2.sort()
        return list_of_string1 == list_of_string2


