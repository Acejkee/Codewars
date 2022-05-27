def enough(cap, on, wait):
    if (on + wait) <= cap:
        return 0
    elif (on + wait) > cap:
        return abs(on + wait -cap)