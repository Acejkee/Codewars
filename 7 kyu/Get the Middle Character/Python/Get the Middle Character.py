def get_middle(x):
    if len(x)%2 == 0: 
        return x[int(len(x)/2)-1] + x[int(len(x)/2)]

    else: 
        return x[int(len(x)/2)]