def descending_order(num):
    num = str(num)
    num = ''.join(num)
    num = list(num)
    num = sorted(num)
    return int(''.join(reversed(num)))
    