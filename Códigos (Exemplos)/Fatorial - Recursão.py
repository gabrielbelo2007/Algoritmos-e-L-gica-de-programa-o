def fat(x, z, w):
    if x == 1:
        return x
    else:
        z += x
        if z != x:
            z -= x
        y = z * (x - 1)
        w += y
        print(w)
        fat(x - 1, x, 0)

fat(4, 4, 0)
