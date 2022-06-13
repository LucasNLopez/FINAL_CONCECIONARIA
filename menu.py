from numpy import append
from objetos import *
from edit import modifica
from usuarios import *
import os
from agregar import *


def menu_product (user):
    pro_dispo = []
    
    va1 = Autos("Ford K", 2011, 85000, 650000)
    va2 = Autos("Chevrolet Cruze", 2018, 25000, 3500000)
    va3 = Autos("Toyota Yaris", 2020, 23000, 3875000)

    va4 = Bicicletas("Orbea", 29, 160000)
    va5 = Bicicletas("Venzo", 29, 95000)

    va6 = Motos("Honda Wave", 2015, 60000, 75000)
    va7 = Motos("Bajaj Rouser", 2016, 50000, 315000)

    pro_dispo.append(va1)
    pro_dispo.append(va2)
    pro_dispo.append(va3)
    pro_dispo.append(va4)
    pro_dispo.append(va5)
    pro_dispo.append(va6)
    pro_dispo.append(va7)
    
    d=0
    while d != 3:
        if user == 2:
            print("""
            Elige una de las siguentes opciones\n 
            1)Productos\n 
            2)Desconectarse
            """)
            x = int(input())
            j = 1
            while j != 0:
                if x == 1:
                    print("""
                    Seleccione una categoria\n
                     1) Autos\n 
                     2) Motos\n 
                     3) Bicicletas\n 
                     4) Volver \n
                     """)
                    c = int(input())
                    if c == 1:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) ==Autos:
                                print(f"Auto = {pro_dispo[i].marca}\nModelo = {pro_dispo[i].modelo}\nKm = {pro_dispo[i].km}\nPrecio = ${pro_dispo[i].precio}\n---------------\n")
                    elif  c == 2:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) == Motos:
                                print(f"Moto = {pro_dispo[i].marca}\nModelo = {pro_dispo[i].modelo}\nKm = {pro_dispo[i].km}\nPrecio = ${pro_dispo[i].precio}\n---------------\n")
                    elif c == 3:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) == Bicicletas:
                                print(f"Marca Bicicleta = {pro_dispo[i].marca}\nRodado de la Bicicleta = {pro_dispo[i].rodado}\nPrecio = ${pro_dispo[i].precio}\n---------------\n")
                    elif c == 4:
                        input("Vuelva Pronto\nPresione enter para continuar...")
                        os.system("cls")
                        j = 0
                    else:
                        print("Opcion Invalida\n")
                        input("Pulse enter para continuar ...")
                elif x == 2:
                    j = 0
                    d = 3
                else:
                    print("Opcion Invalida\n---------------\n")
        elif user == 1:
            print("""
            Elige una de las siguentes opciones\n 
            1) Productos\n 
            2) Desconectarse\n 
            3) Editar\n
            4) Agregar Vehículo\n
            """)
            x = int(input())
            f = 1
            while f != 0:
                if x == 1:
                    print("""
                    Seleccione una categoria\n 
                    1) Autos\n 
                    2) Motos\n 
                    3) Bicicletas\n 
                    4) Volver\n
                    """)
                    c = int(input())
                    if c == 1:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) == Autos:
                                print(f"Auto = {pro_dispo[i].marca}\nModelo = {pro_dispo[i].modelo}\nKm = {pro_dispo[i].km}\nPrecio = ${pro_dispo[i].precio}\n---------------\n")
                    elif  c == 2:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) == Motos:
                                print(f"Moto = {pro_dispo[i].marca}\nModelo = {pro_dispo[i].modelo}\nKm = {pro_dispo[i].km}\nPrecio = ${pro_dispo[i].precio}\n---------------\n")
                    elif  c == 3:
                        for i in range(len(pro_dispo)):
                            if type(pro_dispo[i]) == Bicicletas:
                                print(f"Bicicleta  = {pro_dispo[i].marca}\nRodado = {pro_dispo[i].rodado}\nPrecio = ${pro_dispo[i].precio}\n")
                    elif c == 4:
                        input("Presione enter para volver...\n")
                        os.system("cls")
                        f = 0
                    else:
                        print("Opcion Invalida\n")
                        input("Presione enter para continuar...")
                elif x == 2:
                    f = 0
                    d = 3
                elif x == 3:
                    os.system("cls")
                    pro_dispo = modifica(pro_dispo)
                    f = 0
                elif x == 4:
                    print("""
                    Seleccione una categoria\n 
                    1) Autos\n 
                    2) Motos\n 
                    3) Bicicletas\n 
                    4) Volver\n
                    """)
                    agr= int(input())
                    if agr ==1:
                        pro_auto= agregar_vehiculo(agr)
                        pro_dispo.append(pro_auto)
                        
                    elif agr ==2:
                        pro_moto= agregar_vehiculo(agr)
                        pro_dispo.append(pro_moto)
                        
                        
                    elif agr == 3:
                        pro_bici= agregar_vehiculo(agr)
                        pro_dispo.append(pro_bici)
                        
                    elif agr == 4:
                        input("Presione enter para volver...\n")
                        os.system("cls")
                        f=0
    return d