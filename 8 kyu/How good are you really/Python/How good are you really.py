def better_than_average(c, y):
    if (sum(c) / len(c)) < y:
        return True
    else:
        return False