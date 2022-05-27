def calculator(x,y,op):
    if (type(x) == int) and (type(y) == int) and op =='+':
        return x + y    
    if (type(x) == int) and (type(y) == int) and op =='-':
        return x - y
    if (type(x) == int) and (type(y) == int) and op =='*':
        return x * y
    if (type(x) == int) and (type(y) == int)and op =='/':
        return x / y
    else:
        return "unknown value"