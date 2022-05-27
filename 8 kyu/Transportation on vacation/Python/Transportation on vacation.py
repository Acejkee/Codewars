def rental_car_cost(d):
    res = d * 40
    if 3<=d<7:
        return (res-20)
    elif d >= 7:
        return (res-50)
    else:
        return res