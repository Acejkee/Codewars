def fake_bin(x):
    sum = ''
    for i in x:
        if i == '0' or i == '1' or i == '2' or i == '3' or i == '4':
            sum += '0'
        else:
            sum += '1'
    return sum
    