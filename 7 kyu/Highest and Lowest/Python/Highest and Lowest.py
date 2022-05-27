def high_and_low(numbers):
    high = max([int(x) for x in numbers.split()])
    low = min([int(x) for x in numbers.split()])
    return str(high) + ' ' + str(low)