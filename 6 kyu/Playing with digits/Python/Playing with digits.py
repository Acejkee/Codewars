def dig_pow(n, p):
    sub = p
    result = 0
    for i in str(n):
        result += int(i)**p
        p+=1
    print(result)
    if (result % n == 0):
        return result / n
    else:
        return -1