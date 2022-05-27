# return masked string
def maskify(cc):
    a = '#'
    if len(cc) <= 4:
        return cc
    else:
        return a * len(cc[0:-4]) + cc[-4:]
        