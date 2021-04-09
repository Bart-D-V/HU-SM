# congruential number generator.
def congruential(Xn, a, c, m):
    while True:
        Xn = (a * Xn + c) % m
        yield Xn
