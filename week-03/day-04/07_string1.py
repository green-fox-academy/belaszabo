# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.
string = 'adxxffoxxxtx'

def changing(string):
    if string == '':
        return ''
    elif string[0] == 'x':
        return 'y' + changing(string[1:])
    else:
        return string[0] + changing(string[1:])

print(changing(string))