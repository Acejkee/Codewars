def spin_words(s):
    m = []
    s = s.split()
    for i in s:
        if len(i) >= 5:
            m.append(i[::-1])
        else:
            m.append(i)
    return ' '.join(m)
            
            
    