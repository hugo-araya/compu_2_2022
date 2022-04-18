def mensaje(tipo):
    if tipo == 1:
        print('Esta Normal el Individuo')
    else:
        print('No esta Normal el Individuo')

def lectura(linea):
    linea = linea.rstrip('\n')
    lista = linea.split(';')
    hemo = float(lista[0])
    medicion = lista[1]
    edad = int(lista[2])
    genero = lista[3]
    return hemo, medicion, edad, genero, linea

def meses(hemo, edad):
    if edad <= 1:
        if hemo>= 13 and hemo <= 26:
            mensaje(1)
        else:
            mensaje(2)
    elif edad <= 6:
        if hemo >= 10 and hemo <=18:
            mensaje(1)
        else:
            mensaje(2)
    else:
        if hemo >= 11 and hemo <= 15:
            mensaje(1)
        else:
            mensaje(2)

def agnos(hemo, edad, genero):
    if edad <= 15:
        if edad <= 5:
            if hemo >= 11.5 and hemo <= 15:
                mensaje(1)
            else:
                mensaje(2)
        elif edad <= 10:
            if hemo >= 12.6 and hemo <= 15.5:
                mensaje(1)
            else:
                mensaje(2)
        else:
            if hemo >= 13 and hemo <= 15.5:
                mensaje(1)
            else:
                mensaje(2)       
    else:
        if genero == '0':
            if hemo >= 14 and hemo <= 18:
                mensaje(1)
            else:
                mensaje(2)
        else:
            if hemo >= 12 and hemo <= 16:
                mensaje(1)
            else:
                mensaje(2)

def depura1(linea):
    print(linea)

if __name__ == "__main__":
    ar = open('datos.txt')
    for linea in ar:
        #depura1(linea)
        hemo, medicion, edad, genero , linea= lectura(linea)
        #depura1(linea)
        if medicion == '0':
            meses(hemo, edad)
        else:
           agnos(hemo, edad, genero) 


