def max_multiple(a, b):
    sum = 0
    for i in range(1,b+1):
        if i % a == 0 and i > sum:
            sum = i
    return sum