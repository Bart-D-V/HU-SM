seed = '2398412837'


def middel_square(seed):
    output = []
    middel = len(seed)

    while len(output) == len(set(output)):
        square = str(int(seed) ** 2)

        if middel % 2 == 0:
            square = square.zfill(middel * 2)
        else:
            square = square.zfill(middel)

        y = int((len(square) - middel) / 2)
        seed = int(square[y:y + middel])

        output.append(seed)

    return output


def middel_square1(seed, n):
    output = []
    middel = len(seed)

    while len(output) <= n:
        square = str(int(seed) ** 2)

        if middel % 2 == 0:
            square = square.zfill(middel * 2)
        else:
            square = square.zfill(middel)

        y = int((len(square) - middel) / 2)
        seed = int(square[y:y + middel])

        for i in str(seed):
            output.append(int(i))

    return output


list = middel_square(seed)
print(list)
