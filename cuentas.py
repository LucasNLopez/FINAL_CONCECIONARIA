from usuarios import *
import os
cuentas = []
cuenta_invitado=Invitado("invitado@gmail.com","123")
cuenta_administrador=Administrador("lucaslopez@gmail.com","admin123")

cuentas.append(cuenta_invitado)
cuentas.append(cuenta_administrador)

def validar(seleccion):
    lu=3
    while lu != 0:
        if seleccion == 1:
            print("BIENVENIDO AL MENU ADMINISTRADOR")
            print("Ingrese el e-mail y luego la contraseña")
            mail = input ()
            contraseña = input ()
            for i in range(len(cuentas)):
                if mail == cuenta_administrador.user and contraseña == cuenta_administrador.contraseña:
                    return cuentas[i]
        elif seleccion == 2:
            print ("MENU INVITADO")
            print ("Ingrese e-mail y contraseña")
            mail = input ()
            contraseña = input ()
            for i in range(len(cuentas)):
                if mail == cuenta_invitado.user and contraseña == cuenta_invitado.contraseña:
                    return cuentas[i]
        elif seleccion == 3:
            lu = 0
            os.system("cls")
            print("Hasta Luego.")