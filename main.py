from objetos import *
from cuentas import *
from usuarios import *
from edit import *
from menu import *
import os


selecc = []
sel = 0
while sel != 3:
    print("""\nseleccione: \n
    1) Menu Administrador\n
    2) Invitado\n 
    3) Salir\n""")
    sel = int(input())
    if sel == 1:
        os.system("cls")
        selecc = validar(sel)
        salida = menu_product(sel)
        sel = salida
    elif sel == 2:
        os.system("cls")
        invit = validar(sel)
        salida = menu_product(sel)
        sel = salida
    elif sel == 3:
        input("Hasta pronto...")
        os.system("cls")
