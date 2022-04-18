vocales = "aeiou"
linea = "esta es una linea de ejemplo para la prueba"
i = 0
cont = 0
while i < len(vocales):
     cont = cont + linea.count(vocales[i])
     i = i + 1
print (cont)
