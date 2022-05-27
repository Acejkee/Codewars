def warn_the_sheep(a):
        a.reverse()
        if 'wolf' in a and 'wolf' != a[0]:
            return "Oi! Sheep number " + str((a.index('wolf'))) + "! You are about to be eaten by a wolf!"
        else:
            return 'Pls go away and stop eating my sheep'