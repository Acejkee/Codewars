def duplicate_count(text):
    text = text.lower()
    result = []
    for i in text:
        if text.count(i) > 1:
            result.append(i)
    return len(set(result))
    






     