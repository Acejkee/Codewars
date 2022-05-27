def square_digits(num):
    res = ''
    for i in str(num):
        res = res + str((int(i))**2)
    return int(res)
    pass