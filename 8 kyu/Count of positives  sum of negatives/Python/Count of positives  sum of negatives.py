def count_positives_sum_negatives(arr):
    sum = 0
    count = 0
    for i in arr:
        if i <= 0:
            sum += i
        if i > 0:
            count += 1
    if arr == []:
        return []
    return [count , sum]