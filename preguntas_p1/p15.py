lista1 = [1, 6, 5, 4, 8]
lista2 = [5, 2, 9]
c = []
var1 = len(lista1)
var2 = len(lista2)
if var1 < var2:
    m = var1
else:
	m = var2
for i in range(m):
	c.append(lista1[i] + lista2[i])
c = c + lista1[m:] + lista2[m:]
print ( c )

