def two_sort(array):
    res = ''
    a = sorted(array)
    for i in a[0]:
        res += i + '***'
    return res[:-3]