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


    def count_letters(self, string):
        dict_of_string = {}

        for i in range(len(string)):
            if string[i] in dict_of_string:
                dict_of_string[string[i]] += 1
            else:
                dict_of_string[string[i]] = 1 

        return dict_of_string


    def fibonacci(self, n):
        if type(n) != int or n < 0:
            return "Please enter a non-negative integer"
        if n < 2:
            return n
        else:
            return (self.fibonacci(n-1) + self.fibonacci(n-2))
        