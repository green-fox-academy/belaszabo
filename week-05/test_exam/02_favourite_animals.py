# The program's aim is to collect your favourite animals and store them in a text file.
# There is a given text file called '''favourites.txt''', it will contain the animals
# If ran from the command line without arguments
# It should print out the usage:
# ```fav_animals [animal] [animal]```
# You can add as many command line arguments as many favourite you have.
# One animal should be stored only at once
# Each animal should be written in separate lines
# The program should only save animals, no need to print them

from sys import argv

class FavouriteAnimal(object):

    def __init__(self):
        self.file_name = "favourites.txt"
        if len(argv) == 1:
            self.usage()
        else:
            self.is_in_file()

    def usage(self):
        print("02_favourite_animals.py [animal] [animal]...")
        
    def is_in_file(self):
        # print("checking if in file")
        f = open(self.file_name, "r")
        lines = f.readlines()
        f.close()
        for i in range(1, len(argv)):
            if argv[i] + "\n" not in lines:
                self.add_fav(argv[i])

    def add_fav(self, arg):
        f = open(self.file_name, "a")
        f.write(arg + "\n")
        f.close()

favs = FavouriteAnimal()