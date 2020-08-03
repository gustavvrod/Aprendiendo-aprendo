<<<<<<< HEAD

class Domicilio():
    def __init__(self, id: int):
        self.id= id
        self.direccion= input("ingrese su direccion: ")
        self.comuna= input("ingrese su comuna: ")
        self.numero= input("ingrese el numero de la casa: ")

    def get_id(self):
        return self.id 
    def set_id(self,id: int):
        self.id= id
    def get_direccion(self):
        return self.direccion 
    def set_direccion(self,direccion: str):
        self.direccion= direccion
    def get_comuna(self):
        return self.comuna
    def set_comuna(self,comuna: str):
        self.comuna= comuna    
    def get_numero(self):
        return self.numero 
    def set_numero(self,numero: int):
        self.numero= numero
    

if __name__ == "__main__":
    Domicilio = Domicilio(id=1)
    print(Domicilio.get_direccion())
    print(Domicilio.get_comuna())
    print(Domicilio.get_numero())



  

=======

class Domicilio():
    def __init__(self, id: int):
        self.id= id
        self.direccion= input("ingrese su direccion: ")
        self.comuna= input("ingrese su comuna: ")
        self.numero= input("ingrese el numero de la casa: ")

    def get_id(self):
        return self.id 
    def set_id(self,id: int):
        self.id= id
    def get_direccion(self):
        return self.direccion 
    def set_direccion(self,direccion: str):
        self.direccion= direccion
    def get_comuna(self):
        return self.comuna
    def set_comuna(self,comuna: str):
        self.comuna= comuna    
    def get_numero(self):
        return self.numero 
    def set_numero(self,numero: int):
        self.numero= numero
    

if __name__ == "__main__":
    Domicilio = Domicilio(id=1)
    print(Domicilio.get_direccion())
    print(Domicilio.get_comuna())
    print(Domicilio.get_numero())



  

>>>>>>> 1c9b3fe7fa8ff626d39cf70b9be4a6d30c839497
