def reverse(st):
    a = []
    for i in st.split():
        a.insert(0,i)
    return ' '.join(a)