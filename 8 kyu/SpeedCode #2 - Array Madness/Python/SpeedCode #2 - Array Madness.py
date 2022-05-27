def array_madness(a,b):
    sum_a = 0
    sum_b = 0
    for i in a:
        i = i**2
        sum_a += i
    for j in b:
        j = j**3
        sum_b += j
    if sum_a > sum_b:
        return True
    else:
        return False
        