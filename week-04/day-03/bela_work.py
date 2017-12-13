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
