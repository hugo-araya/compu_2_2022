

def mensaje(tipo):
    if tipo == 1:
        print('El valor esta en su rango')
    else:
        print('La medicion no esta en el rango adecuado')

def limpia(linea):
    linea = linea.rstrip('\n')
    lista = linea.split(';')
    hemo = float(lista[0])
    medicion = lista[1]
    edad = int(lista[2])
    genero = lista[3]
    return hemo, medicion, edad, genero

def pregunta(valor1, valor2):
    if hemo >= valor1 and hemo <= valor2:
        mensaje(1)
    else:
        mensaje(2)    

def meses(hemo, edad):
    if edad <= 1:
        pregunta(13, 26)
    elif edad <= 6:
        pregunta(10,18)
    else:
        pregunta(11,15)           

def agnos(hemo, edad,genero):
    if edad <= 15:
        if edad <= 5:
            pregunta(11.5,15)
        elif edad <= 10:
            pregunta(12.6,15.5)
        else:
            pregunta(13,15.5)                          
    else:
        if genero == '0':
            pregunta(14,18)    
        else:
            pregunta(12,16)                


if __name__ == '__main__':
    ar = open('sangre.txt')
    for linea in ar:
        hemo, medicion, edad, genero = limpia(linea)
        print(hemo, medicion, edad, genero)
        if medicion == '0':
            meses(hemo, edad)
        else:
            agnos(hemo, edad, genero)
