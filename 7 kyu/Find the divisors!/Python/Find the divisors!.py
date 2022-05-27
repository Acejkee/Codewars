def divisors(inter):
    arr = []
    for x in range(2,inter): 
        if inter % x == 0:
            arr.append(x)
    if len(arr) == 0:
        return f'{inter} is prime'
    else:    
        return arr
    