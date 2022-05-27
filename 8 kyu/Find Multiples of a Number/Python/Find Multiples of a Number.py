def find_multiples(i, l):
    c = []
    for g in range(i,l+1):
        if g % i == 0 or g % l+1 == 0:
            c.append(g)
    return c
        