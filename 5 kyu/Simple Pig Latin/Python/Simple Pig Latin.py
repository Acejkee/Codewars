def pig_it(text):
    words = text.split(" ")
     
    new_words = []
     
    for word in words:
        if word.isalpha():
            new_word = word[1:] + word[0] + "ay"
            new_words.append(new_word)
        else:
            new_words.append(word)
    return " ".join(new_words)
        
        