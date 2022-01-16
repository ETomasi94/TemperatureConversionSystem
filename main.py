def fromC(x): return x


def toC(x): return x


def fromDe(x): return 100 - x * 2 / 3


def toDe(x): return (100 - x) * 3 / 2


def fromF(x): return (x - 32) * 5 / 9


def toF(x): return x * 9 / 5 + 32


def fromK(x): return x - 273.15


def toK(x): return x + 273.15


def fromN(x): return x * 100 / 33


def toN(x): return x * 33 / 100


def fromR(x): return (x - 491.67) * 5 / 9


def toR(x): return x * 9 / 5 + 491.67


def fromRé(x): return x * 5 / 4


def toRé(x): return x * 4 / 5


def fromRø(x): return (x - 7.5) * 40 / 21


def toRø(x): return x * 21 / 40 + 7.5


toT = {'F': toF, 'K': toK, 'R': toR, 'De': toDe, 'N': toN, 'Ré': toRé, 'Rø': toRø, 'C': toC}

fromT = {'F': fromF, 'K': fromK, 'R': fromR, 'De': fromDe, 'N': fromN, 'Ré': fromRé, 'Rø': fromRø, 'C': fromC}


def fromTtoAll(n, t):
    celsius = fromT[t](n)
    return {scale: convert(celsius) for scale, convert in toT.items()}


def table(n):
    tot = [[v for k, v in sorted(fromTtoAll(n, t).items(), key=lambda x: x[0])]
            for t in sorted(toT.keys())]
    res = " " + (8 * "{: ^6} ") + "\n" + (8 * ("{:<3}" + (8 * "{: 6.1f} ") + "\n"))
    tmp = vres = sorted(toT.keys())

    for i in range(8): vres += [tmp[i]]+tot[i]

    return res.format(*vres)


if __name__ == "__main__":

    print(fromTtoAll(30, 'C'))

    print(table(30))
