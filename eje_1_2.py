#!/usr/bin/python
# -*- coding: utf-8 -*-
# Autor: Hugo Araya Carrasco
# Fecha: 28/03/2022
# Version: 1.0

# import <biblioteca>

#Declaración de funciones.

if __name__ == "__main__":
    precio = int(input("Ingrese el precio: "))
    mes = int(input("Mes: "))
    pagar = precio
    if (mes >= 3 and mes <= 5):
        pagar = precio*0.87
    print("A pagar: ", pagar)

