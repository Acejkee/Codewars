def find_outlier(integers):
    result = list(filter(lambda x: x%2 == 0 , integers))
    arr = list(filter(lambda x: x%2 == 1 , integers))
    if (len(result) == 1):
        return result[0]
    else:
        return arr[0]