def digitize(n):
    return [int(i) for i in str(n)[::-1]]


print(digitize(35231))


# while my answer was pretty good - the best practice and clever answer was
def digitize(n):
    return map(int, str(n)[::-1])