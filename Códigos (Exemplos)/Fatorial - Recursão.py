def fat(x, w):
    if x <= 1:
        print(w)
        return
    if w == 0:
        w = x * (x-1)
        fat(x-1, w)
    else:
        w = w * (x-1)
        fat(x-1, w)

fat(7, 0)

# Nota do autor

"""
def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)

print(fat(4))
"""