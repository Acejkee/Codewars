def points(games):
    sum = 0
    for game in games:
        if game[0] > game[2]:
            sum = sum + 3
        elif game[0] < game[2]:
            sum = sum + 0
        else:
            sum = sum + 1
    return sum