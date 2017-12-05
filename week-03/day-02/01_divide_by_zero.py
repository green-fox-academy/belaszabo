def divide_ten(number):
    try:
        print (10 / number)
    except ZeroDivisionError:
        print ('fail')

divide_ten(0)