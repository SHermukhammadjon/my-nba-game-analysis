def box(word, size):
    box = str(word)
    while len(box) != size:
        if len(box) < size:
            box = box + " "
        elif len(box) > size:
            box = box[0:-2]

    return box


def column(series):
    n=0
    for key in series.keys():
        n+=1
        if n == 1:
            print(box(key, 15), end = "|")
        else:
            print(box(key, 5), end = "|")
    print()


def series(series):
    n = 0
    for key, value in series.items():
        # print(type(value), end = " ")
        n+=1
        if n == 1:
            print(box(value, 15), end = "|")
        else:
            print(box(value, 5), end = "|")
    print()