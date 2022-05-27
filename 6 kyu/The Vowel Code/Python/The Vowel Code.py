def encode(st):
    sum = ''
    for i in st:
        if i == 'a':
            sum += '1'
        elif i == 'e':
            sum += '2'
        elif i == 'i':
            sum += '3'
        elif i == 'o':
            sum += '4'
        elif i == 'u':
            sum += '5'
        else:
            sum += i
    return sum
    
def decode(st):
    sum = ''
    for i in st:
        if i == '1':
            sum += 'a'
        elif i == '2':
            sum += 'e'
        elif i == '3':
            sum += 'i'
        elif i == '4':
            sum += 'o'
        elif i == '5':
            sum += 'u'
        else:
            sum += i
    return sum