def combat(health, damage):
    new = health - damage
    if new <= 0:
        return 0
    return new