
class Genero():
    def __init__ (self, id: int):
        self.genero= ""
        if id == 1: 
            self.genero="masculino"
        if id == 2:
            self.genero="femenino"
        if id == 3:
            self.genero="transgenero"
        if id == 4:
            self.genero="transexual"      
    
    def get_genero(self):
        return self.genero 
    def set_genero(self, id: int):
        if id == 1: 
            self.genero="masculino"
        if id == 2:
            self.genero="femenino"
        if id == 3:
            self.genero="transgenero"
        if id == 4:
            self.genero="transexual"
            













