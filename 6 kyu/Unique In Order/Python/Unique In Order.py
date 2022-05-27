def unique_in_order(iter):
    new = ''
    back = []
    for i in iter:
        if i!=new:     
            back.append(i)     
        new=i     
    return back
        