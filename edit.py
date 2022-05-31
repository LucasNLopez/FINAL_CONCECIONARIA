from objetos import *

def modifica (product):
    var=""
    j=1
    while j != 0:
        print("Seleccione una categoria a modificar\n 1- Autos\n 2- Motos\n 3- Bicicletas\n 4- Salir\n")
        c = int(input())
        if c == 1:
            for i in range(len(product)):
                if type(product[i]) == Autos:
                    print(f"""Auto = {product[i].modelo}\nKm = {product[i].km}\nPrecio = {product[i].precio}\n""")
                    print("Si desea Modificarlo Escriba [Modificar] en caso contrario escriba [No]\n")
                    var = input()
                    var = var.lower()
                    if var == "modificar":
                        product[i].modelo = input("Ingrese el modelo\n")
                        product[i].km = int(input("Indique los Kilomentros del Vehiculo\n"))
                        product[i].Precio = int(input("Indique el Valor del Vehiculo\n"))
                    elif var == "no":
                        print("Pasando al siguiente Vehiculo...\n")
        elif  c == 2:
            for i in range(len(product)):
                if type(product[i]) == Motos:
                    print(f"""Moto = {product[i].modelo}\nKm = {product[i].km}\nPrecio = {product[i].precio}\n""")
                    print("Si desea Modificarlo Escriba [Modificar] en caso contrario escriba [No]\n")
                    var = input()
                    var = var.lower()
                    if var == "modificar":
                        product[i].modelo = input("Ingrese el modelo\n")
                        product[i].km = int(input("Indique los Kilomentros del Vehiculo\n"))
                        product[i].Precio = int(input("Indique el Valor del Vehiculo\n"))
                    elif var == "no":
                        print("Pasando al siguiente Vehiculo...\n")
        elif  c == 3:
            for i in range(len(product)):
                if type(product[i]) == Bicicletas:
                    print(f"""Bicicleta = {product[i].marca}\nRodado = {product[i].rodado}\nPrecio = {product[i].precio}\n""")
                    print("Si desea Modificarlo Escriba [Modificar] en caso contrario escriba [No]\n")
                    var = input()
                    var = var.lower()
                    if var == "modificar":
                        product[i].marca = input("Ingrese la marca\n")
                        product[i].rodado = int(input("Indique el rodado\n"))
                        product[i].precio = int(input("Indique el precio\n"))
                    elif var == "no":
                        print("Pasando al siguiente Vehiculo...\n")
        elif c == 4:
            j = 0
            print("Vuelva Pronto\n")
            input("Pulse enter para continuar...")
        else:
            print("Opcion Invalida....")
    return(product)