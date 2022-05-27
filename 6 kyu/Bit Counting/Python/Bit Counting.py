def count_bits(n):
    sum = 0
    a = bin(n)
    a = list(a)
    for i in a:
        if i == '1':
            sum += 1
    return sum