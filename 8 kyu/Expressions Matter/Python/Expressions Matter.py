def expression_matter(a, b, c):
    result = []
    sum = a * (b + c)
    sum2 = a * b * c
    sum3 = a + (b * c)
    sum4 = (a + b) * c
    sum5 = a + b + c
    result.append(sum)
    result.append(sum2)
    result.append(sum3)
    result.append(sum4)
    result.append(sum5)
    return max(result)