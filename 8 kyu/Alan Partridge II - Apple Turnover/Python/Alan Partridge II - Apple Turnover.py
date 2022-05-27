def apple(x):
    if type(x) == int:
        if x**2 > 1000:
            return "It's hotter than the sun!!"
        else:
            return "Help yourself to a honeycomb Yorkie for the glovebox."
    else:
        x = int(x)
        if x**2 > 1000:
            return "It's hotter than the sun!!"
        else:
            return "Help yourself to a honeycomb Yorkie for the glovebox." 