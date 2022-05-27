def is_valid_walk(walk):
    a = walk.count('n')
    b = walk.count('s')
    c = walk.count('w')
    d = walk.count('e')
    if str(a) == str(b) and str(c) == str(d) and len(walk) == 10:
        return True
    else:
        return False