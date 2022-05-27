def to_jaden_case(string):
    list=string.split(" ")
    for i in range(len(list)):
        list[i] = list[i].capitalize()
    return ' '.join(list)
        
        