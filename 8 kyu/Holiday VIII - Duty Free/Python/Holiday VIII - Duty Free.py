import math
def duty_free(price, discount, holiday_cost):
        new = holiday_cost / (price * (discount / 100))
        return math.floor(new)