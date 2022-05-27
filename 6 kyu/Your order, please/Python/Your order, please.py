def order(words):
    return ' '.join(sorted(words.split(" "), key = lambda x: sorted(x)))
    