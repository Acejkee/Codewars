def add_length(stro):
    p = []
    new = stro.split()
    for i in new:
        p.append(i + ' ' + str(len(i)))
    return p
        