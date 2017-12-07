# Given a string, compute recursively a new string where all the 'x' chars have been removed.
string = 'adxxffoxxxtx'

def changing(string):
    if string == '':
        return ''
    elif string[0] == 'x':
        return '' + changing(string[1:])
    else:
        return string[0] + changing(string[1:])

print(changing(string))