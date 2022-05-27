def persistence(n):
    count = 0;
    while(len(str(n)) != 1):
        count += 1
        sum = 1
        for i in str(n):
            sum *= int(i)
            n = sum
    return count