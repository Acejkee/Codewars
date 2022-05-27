def well(x):
    count = 0
    for i in x:
        if i == 'good':
            count += 1
    if count > 2:
            return 'I smell a series!'
    elif count == 1 or count == 2:
            return 'Publish!'
    else:
            return 'Fail!'
            