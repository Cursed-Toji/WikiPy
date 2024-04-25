def maior(variavel):
    maior_item = variavel[0]
    for item in variavel:
        if item > maior_item:
            maior_item = item

    return maior_item


def menor(variavel):
    menor_item = variavel[0]
    for item in variavel:
        if item <menor_item:
            menor_item = item
    return menor_item

maior([1,2,3,4,25415, 5,6,7,8,9,])
menor([1,2,3,4,25415, 5,6])

print(maior([2,3,4,25415, 5]))
print(menor([1,2,3,4,25415, 5,6]))
