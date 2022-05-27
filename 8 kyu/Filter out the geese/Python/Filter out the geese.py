geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]

def goose_filter(birds):
    output = []
    for i in birds:
        if i not in geese:
            output.append(i)
    return output
              