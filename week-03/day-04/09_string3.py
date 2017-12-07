# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".
string = 'adxxffoxxxtx'

def changing(string):
    if string == '':
        return ''
    elif string[1:] == '':
        return string[0]
    else:
        return string[0] + '*'  + changing(string[1:])

print(changing(string))