def correct(string):
    oper = ''
    for i in string:
        if i == '5':
            oper += 'S'
        elif i == '0':
            oper += 'O'
        elif i == '1':
            oper += 'I'
        else:
            oper += i
    return oper
pass