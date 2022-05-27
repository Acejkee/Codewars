def name_shuffler(pop):
    word = pop.split()
    word = list(reversed(word))
    return ' '.join(word)