import datetime
from domicilios import Domicilio
from genero import Genero


class Persona():
    def __init__(self, id: int, nombre: str, apellido: str, fechadenacimiento: datetime.datetime, genero: int, cedula: str, correo: str, telefono: str, domicilio: Domicilio):
        self.id= id
        self.nombre= nombre
        self.apellido= apellido
        self.fechadenacimiento= fechadenacimiento
        self.genero= Genero(genero)
        self.correo = correo
        self.cedula= cedula
        self.telefono= telefono
        self.domicilios= [domicilio]
    def get_id(self):
        return self.id 
    def set_id(self,id: int):
        self.id= id
    def get_nombre(self):
        return self.nombre 
    def set_nombre(self,nombre: str):
        self.nombre= nombre
    def get_apellido(self):
        return self.apellido 
    def set_apellido(self,apellido: str):
        self.apellido= apellido
    def get_fechadenacimiento(self):
        return self.fechadenacimiento.strftime("%Y-%m-%d")
    def set_fechadenacimiento(self,fechadenacimiento: datetime):
        self.fechadenacimiento= fechadenacimiento
    def get_genero(self):
        return self.genero.get_genero()
    def set_genero(self,id: int):
        self.genero= Genero(id)
    def get_cedula(self):
        return self.cedula 
    def set_cedula(self,cedula: str):
        self.cedula= cedula
    def get_telefono(self):
        return self.telefono 
    def set_telefono(self,telefono: str):
        self.telefono= telefono
    def get_correo(self):
        return self.correo 
    def set_correo(self,correo: str):
        self.correo= correo
    def get_domicilios(self):
        domicilio= self.domicilios[0].get_direccion() + " " + self.domicilios[0].get_comuna() + " " +  self.domicilios[0].get_numero()
        return domicilio
    def set_domicilio(self,domicilio: Domicilio):
        self.domicilios.append(domicilio)
    def get_edad(self):
        return datetime.datetime.now().year-self.get_fechadenacimiento().year
    def get_persona(self):
        return {
            "id":self.get_id(),
            "nombre":self.get_nombre(),
            "apellido":self.get_apellido(),
            "fechadenacimiento":self.get_fechadenacimiento(),
            "genero":self.get_genero(),
            "cedula":self.get_cedula(),
            "telefono":self.get_telefono(),
            "correo":self.get_correo(),
            "domicilio":self.get_domicilios(),
        }
        

if __name__ == "__main__":
    personas=[]
    while True:    
        id= 1
        nombre= input("ingrese su nombre: ")
        apellido= input("ingrese su apellido: ")
        fechadenacimiento= datetime.datetime(year=int(input("ingrese año de nacimiento: ")),month=int(input("ingrese mes de nacimiento: ")),day=int(input("ingrese dia de nacimiento: ")))
        genero=int(input("ingrese id genero:" ))
        correo=input("ingrese su correo: ")
        cedula=input("ingrese su cedula: ")
        telefono=input("ingrese su telefono: ")
        domicilios=Domicilio(id)
        persona= Persona(id=1, nombre=nombre, apellido=apellido, fechadenacimiento=fechadenacimiento ,genero=genero,cedula=cedula ,telefono=telefono,correo=correo ,domicilio=domicilios)
        personas.append(persona)
        print(persona.get_persona())
        
        id= id + 1
        respuesta= input("quieres ingresar otro?: ")
        if respuesta== "no":
            break
        