#!/usr/bin/python
# -*- coding: utf-8 -*-
# Autor: Hugo Araya Carrasco
# Fecha: 28 / 03 /2022
# Version: 1.0
# Descripción: Bla Bla Bla ...

#import <biblioteca>

#Declaración de funciones.

if __name__ == "__main__":
    precio = int(input('Precio: '))
    mes = input("Mes: ")
    mes = mes.lower()
    meses = ['enero', 'febrero', 'marzo', 'abril','mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    if mes in meses:
        mes_descuento = ['marzo', 'abril', 'mayo']
        pagar = precio
        if mes in mes_descuento:
            pagar = precio * 0.87
        print("A pagar: ", pagar)
    else:
        print('El mes no existe.')