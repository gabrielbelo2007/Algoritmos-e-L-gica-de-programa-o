def fat(x, z, w):
    z -= 1
    y = x-1
    if z == y:
        w = x * z
        z -= 1
    if z <= 1:
        print(w)
    else:
        w = w * z
        fat(x, z, w)

fat(7, 7, 0)
