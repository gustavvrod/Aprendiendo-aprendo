from contrasena import Contrasena

class Usuario():
    def __init__(self,nombre:str,contrasena:Contrasena,correo:str):
        self.id=0
        self.nombre= nombre
        self.contrasena= contrasena
        self.correo= correo
        self.activo=True
    
    
    def get_id(self):
        return self.id 
    def set_id(self,id: int):
        self.id= id
    def get_nombre(self):
        return self.nombre 
    def set_nombre(self,nombre: str):
        self.nombre= nombre
    def get_contrasena(self):
        return self.contrasena 
    def set_contrasena(self,contrasena: str):
        self.contrasena.set_contrasena(contrasena)
    def get_correo(self):
        return self.correo 
    def set_correo(self,correo: str):
        self.correo= correo 
    def get_activo(self):
        return self.activo
    def set_activo(self, activo:bool):
        self.activo= activo

