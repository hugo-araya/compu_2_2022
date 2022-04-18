lista1= [1, 2, 3]
lista2= [1, 2, 3]
for elemento in lista2:
    lista1.append (elemento)
lista2 = lista2 + [4]
lista1[-1] = 100
del lista2[0]
lista3= lista2
print (lista1)


