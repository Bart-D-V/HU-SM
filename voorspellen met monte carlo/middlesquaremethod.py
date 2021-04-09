# middel square random number generator
def middel_square(seed):
    middel = len(seed)

    while True:
        square = str(int(seed) ** 2)

        if middel % 2 == 0:
            square = square.zfill(middel * 2)
        else:
            square = square.zfill(middel)

        y = int((len(square) - middel) / 2)
        seed = int(square[y:y + middel])
        output = int(square[y:y + 2])

        yield output