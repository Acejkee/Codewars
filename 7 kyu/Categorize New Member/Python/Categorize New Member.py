def open_or_senior(data):
    new = []
    for i in data:
        if i[0] >= 55 and i[1] > 7:
            new.append('Senior')
        else:
            new.append('Open')
    return new