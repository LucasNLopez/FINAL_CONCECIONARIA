from objetos import *
import os

def agregar_vehiculo(choice):
    if choice == 1:
        print("Ingrese los datos del Vehículo: \n")
        marca_auto=input("Ingrese la marca del Vehículo: \n")
        modelo_auto=int(input("Ingrese el modelo del Vehículo: \n"))
        km_auto=int(input("Ingrese el KM del vehículo: \n"))
        precio_auto=int(input("Ingrese el precio del Vehículo: \n"))
        auto_nuevo=Autos(marca_auto,modelo_auto,km_auto,precio_auto)
        print(auto_nuevo.marca,auto_nuevo.modelo,auto_nuevo.km,auto_nuevo.precio)
    elif choice == 2:
            print("Ingrese los datos de la moto.")
            marca_moto= input("Ingrese la marca: \n")
            modelo_moto=int(input("Ingrese el modelo: \n"))
            km_moto=int(input("Ingrese el KM: \n"))
            precio_moto=int(input("Ingrese el Precio: \n"))
            moto_nueva=Motos(marca_moto,modelo_moto,km_moto,precio_moto)
            print(moto_nueva.marca,moto_nueva.modelo,moto_nueva.precio)
    elif choice == 3:
        print("Ingrese los datos de la Bicicleta: \n")
        marca_bici=input("Ingrese la marca de la Bicicleta: \n")
        rodado_bici=int(input("Ingrese el rodado de la Bicicleta: \n"))
        precio_bici=int(input("Ingrese el precio de la Bicicleta: \n"))
        bici_nueva=Bicicletas(marca_bici,rodado_bici,precio_bici)
        print(bici_nueva.marca,bici_nueva.rodado,bici_nueva.precio)
    elif choice == 4:
        return