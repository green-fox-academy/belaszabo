# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
elements = [4, 8, 12, 16]

def isinl(lon):
  a = 0
  for i in lon:
      if i == 4 or i == 8 or i == 12 or i == 16:
          a += 1
      else:
          a += 0
  if a == len(elements):
      print("True")
  else:
      print("False")

isinl(list_of_numbers)