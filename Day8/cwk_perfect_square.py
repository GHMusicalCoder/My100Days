import math

def find_next_square(sq):
    x = math.sqrt(sq)
    return (x + 1) * (x + 1) if x = math.floor(x) else -1


# best practice
def bp_find_next_square(sq):
    return ((sq ** 0.5) + 1) ** 2 if (sq ** 0.5).is_integer() else -1