def bonus_time(salary, bonus):
    if bonus == True:
        salary *= 10
        return "$" + str(salary)
    else:
        return "$" + str(salary)