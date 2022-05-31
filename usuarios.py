class Invitado():
    def __init__(self,user,contra):
        self.user=user
        self.contraseña=contra
        self.conectado = False 
        self.intentos = 2
        self.seguridad = 2
        
        

class Administrador():
    def __init__(self,user,contra):
        self.user=user
        self.contraseña=contra
        self.conectado = False 
        self.intentos = 2
        self.seguridad = 1
        

