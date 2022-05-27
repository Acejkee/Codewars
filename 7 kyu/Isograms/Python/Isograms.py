def is_isogram(string):
    result = list(string.lower())
    return len(result) == len(set(result))