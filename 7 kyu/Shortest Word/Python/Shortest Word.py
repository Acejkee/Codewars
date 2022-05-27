def find_short(s):
    new = s.split()
    l = 10000
    for i in new:
        if len(i) < l:
            l = len(i)
    return l