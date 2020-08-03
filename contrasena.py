<<<<<<< HEAD

class Contrasena():
    def __init__(self,contrasena:str):
        self.contrasena=contrasena

    def get_contrasena(self):
        return "*"*(len(self.contrasena))
    def set_contrasena(self,contrasena:str):
        if len(contrasena) >= 6:
            self.contrasena=contrasena
            return False
        else:
            return True
    def valida_contrasena(self,contrasena:str):
        if contrasena == self.contrasena:
            return False
        else:
            return True
     
        



if __name__ == "__main__":
    contrasena=Contrasena(input("ingrese contrasena a crear: "))
    print(contrasena.__dict__)

=======

class Contrasena():
    def __init__(self,contrasena:str):
        self.contrasena=contrasena

    def get_contrasena(self):
        return "*"*(len(self.contrasena))
    def set_contrasena(self,contrasena:str):
        if len(contrasena) >= 6:
            self.contrasena=contrasena
            return False
        else:
            return True
    def valida_contrasena(self,contrasena:str):
        if contrasena == self.contrasena:
            return False
        else:
            return True
     
        



if __name__ == "__main__":
    contrasena=Contrasena(input("ingrese contrasena a crear: "))
    print(contrasena.__dict__)

>>>>>>> 1c9b3fe7fa8ff626d39cf70b9be4a6d30c839497
