from distutils.command.config import config
from email.mime import image
from textwrap import fill
from tkinter import *
from turtle import bgcolor
from objetos import *
from cuentas import *
from usuarios import *
from edit import *
from menu import *
import os
from objetos import *
from cuentas import *
from usuarios import *
from edit import *
from menu import *
import os
from agregar import *
##cursor = hand2 ( cambio de cursor para ponerselo en un frame)
    

root = Tk()
root.title("Panel")
root.iconbitmap("auto.ico")
root.geometry("800x550")
root.config(bd=18)
root.config(relief="groove")
root.config(bg="#5458C2")
#TITULO CONCESIONARIA VISUAL
titleFrame=Frame(root)
titleFrame.pack(fill="x")
titleFrame.config(bg="#5458C2",bd=5,relief="ridge")
miImagen=PhotoImage(file="auto.gif")
imagenlabel=Label(image=miImagen,bg="black", width=800, height=70) #IMAGEN DE AUTO NEGRO !!!!!!
imagenlabel.pack(fill="x")
title_font=("Courier",20,"bold")
titlelabel=Label(titleFrame, text="CONCESIONARIA",font=title_font)
titlelabel.config(bg="#5458C2")
titlelabel.pack()

#########LOGGIN DEL PROGRAMA
miFrame=Frame(root)
miFrame.pack()
miFrame.config(bg="#5458C2")
#### Entrada de usuario
usuario=Entry(miFrame)
usuario.grid(row=0,column=1,padx=5,pady=5)
usuario.config(justify="center")
#### Entrada de contraseña
contraseña=Entry(miFrame,)
contraseña.grid(row=1,column=1,padx=5,pady=5)
contraseña.config(justify="center",show="*")

texto_usuario=Label(miFrame,text="Usuario:",bg="#5458C2")
texto_usuario.grid(row=0,column=0,sticky="e",padx=5,pady=5)


texto_contra=Label(miFrame,text="Contraseña:",bg="#5458C2")
texto_contra.grid(row=1,column=0,sticky="w",padx=5,pady=5)

#BOTON ENVIAR LOGGIN
botonEnviar=Button(root, text="Enviar",bg="#5458C2",)
botonEnviar.pack()

lista_archivos = os.listdir()









root.mainloop()