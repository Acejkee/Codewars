def remove_exclamation_marks(s):
    new = ''
    for i in s:
        if i != '!':
            new += i
    return new
            