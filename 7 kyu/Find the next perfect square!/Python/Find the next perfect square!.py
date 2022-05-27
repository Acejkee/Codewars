from math import sqrt
def find_next_square(sq):
    a = int(sq**0.5)
    if sqrt(sq) % 1 == 0:
        return (a+1) ** 2
    else:
        return -1