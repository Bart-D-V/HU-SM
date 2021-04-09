def congruential(Xn, a, c, m):
    lst = []

    while len(lst) == len(set(lst)):
        Xn = (a * Xn + c) % m
        lst.append(Xn)
    return lst


def congruential2(Xn, a, c, m):
    while True:
        Xn = (a * Xn + c) % m
        yield Xn


lst = congruential(7829, 378, 2310, 4321)
print(lst)
