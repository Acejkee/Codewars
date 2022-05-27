def string_clean(s):
    dict = {'1' ,'2' ,'3' ,'4' ,'5' ,'6' ,'7' ,'8' ,'9' ,'0'}
    c = []
    s = list(s)
    for i in s:
        if i not in dict:
            c.append(i)
    return ''.join(c)
    