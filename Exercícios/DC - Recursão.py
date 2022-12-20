# Nota do autor

"""
def soma(lista):
    total = 0
    for x in lista:
        total += x
    return total

print(soma([1, 2, 3, 4]))
"""


# Transformar em uma função recursiva

"""
def soma1(lista, total):
    if len(lista) == 1:
        return total + lista[0]
    elif len(lista) > 1:
        for x in lista:
            total += x
            lista.pop(0)
            return soma1(lista, total)


print(soma1([4, 2, 3, 5, 6], 0))
"""

# Contar o numero de itens da lista

"""
def numerar(lista, total):
    if len(lista) >= 1:
        for x in lista:
            total += 1
            lista.pop(0)
            return numerar(lista, total)
    else:
        return total

print(numerar([1, 2, 3], 0))
"""

# Encontrar o valor mais alto em uma lista


def maior(lista, total):
    if len(lista) >= 1:
        for x in lista:
            total = lista[0]
            if total < lista[1]:
                total = lista[1]
                lista.pop(0)
            else:
                lista.pop(1)
        return total

print(maior([1, 2, 7, 3], 0))
