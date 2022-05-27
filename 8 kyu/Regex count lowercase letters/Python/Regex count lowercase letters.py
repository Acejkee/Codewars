def lowercase_count(strng):
    alf = 'abcdefghijklmnopqrstuvwxyz'
    count = 0
    for i in strng:
        if i in alf:
            count += 1
    return count