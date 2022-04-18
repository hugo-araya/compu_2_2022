lista1 = [9, 8, 3, 2, 0, 6, 7, 5, 1, 4]
LIMITE = len(lista1)
for i in range(1, LIMITE):
    for j in range(0, LIMITE - 1):
        if lista1[j] > lista1[j+1]:
            temp = lista1[j]
            lista1[j] = lista1[j+1]
            lista1[j+1] = temp
print (lista1)

