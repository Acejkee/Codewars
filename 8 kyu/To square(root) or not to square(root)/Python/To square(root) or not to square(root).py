import math
def square_or_square_root(arr):
    new = []
    for i in arr:
        if math.sqrt(i) % 1 == 0:
            new.append(math.sqrt(i))
        else:
            new.append(i**2)
    return new
    