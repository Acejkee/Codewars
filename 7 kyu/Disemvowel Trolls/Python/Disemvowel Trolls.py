def disemvowel(string):
    new = ''
    for i in string:
        if i in "aoueiAOUEI":
            new != i
        else:
            new += i
    return new