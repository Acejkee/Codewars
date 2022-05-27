def tribonacci(signature, n):
    f1 = signature[0]
    f2 = signature[1]
    f3 = signature[2]
    result = [f1,f2, f3]
    for i in range(2, n-1):
        f1, f2 , f3 = f2, f3 , f1+f2+f3
        result.append(f3)
    return result[0:n]
    