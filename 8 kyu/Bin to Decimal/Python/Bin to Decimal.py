def bin_to_decimal(inp):
    res = 0
    for i in inp:
        res = res*2 + int(i)
    return res
    pass