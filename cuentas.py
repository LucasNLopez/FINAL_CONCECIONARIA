from usuarios import *
cuentas = []
cuenta_invitado=Invitado("invitado@gmail.com","123")
cuenta_administrador=Administrador("lucaslopez@gmail.com","admin123")

cuentas.append(cuenta_invitado)
cuentas.append(cuenta_administrador)

def validar(seleccion):
    if seleccion == 1:
        print("BIENVENIDO AL MENU ADMINISTRADOR")
        print("Ingrese el e-mail y luego la contraseña")
        mail = input ()
        contraseña = input ()
        for i in range(len(cuentas)):
            if mail == "lucaslopez@gmail.com" and contraseña == "admin123":
                return cuentas[i]
    elif seleccion == 2:
        print ("MENU INVITADO")
        print ("Ingrese e-mail y contraseña")
        mail = input ()
        contraseña = input ()
        for i in range(len(cuentas)):
            if mail == "invitado@gmail.com" and contraseña == "123":
                return cuentas[i]
