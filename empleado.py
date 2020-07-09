from persona import Persona
from domicilios import Domicilio
import datetime

class Empleado(Persona):
    def __init__(self, id:int, persona: Persona, sueldo:int, fechadeingreso:datetime.datetime):
        super().__init__(id=persona.get_id(), nombre=persona.get_nombre(), apellido=persona.get_apellido(), fechadenacimiento=persona.fechadenacimiento ,genero=persona.genero,cedula=persona.get_cedula() ,telefono=persona.get_telefono(),correo=persona.get_correo() ,domicilio=persona.domicilios[0])
        self.id=id
        self.sueldo=sueldo
        self.fechadeingreso=fechadeingreso
    
    
    def get_id(self):
        return self.id
    def set_id(self,id: int):
        self.id= id
    def get_persona(self):
        return self.get_persona()
    def get_sueldo(self):
        return self.sueldo
    def set_sueldo(self, sueldo: int):
        self.sueldo= sueldo
    def get_fechadeingreso(self):
        return fechadeingreso.strftime("%Y-%m-%d")
    def set_fechadeingreso(self, fechadeingreso: datetime):
        self.fechadeingreso=fechadeingreso
    def get_empleado(self):
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
            "sueldo":self.get_sueldo(),
            "fechadeingreso":self.get_fechadeingreso()
        }


if __name__ == "__main__":
    empleados=[]
    while True:    
        id= 1
        sueldo= input ("ingrese sueldo: $")
        fechadeingreso= datetime.datetime(year=int(input("ingrese año de ingreso: ")),month=int(input("ingrese mes de ingreso: ")),day=int(input("ingrese dia de ingreso: ")))
        nombre= input("ingrese su nombre: ")
        apellido= input("ingrese su apellido: ")
        fechadenacimiento= datetime.datetime(year=int(input("ingrese año de nacimiento: ")),month=int(input("ingrese mes de nacimiento: ")),day=int(input("ingrese dia de nacimiento: ")))
        genero=int(input("ingrese id genero:" ))
        correo=input("ingrese su correo: ")
        cedula=input("ingrese su cedula: ")
        telefono=input("ingrese su telefono: ")
        domicilios=Domicilio(id)
        persona= Persona(id=1, nombre=nombre, apellido=apellido, fechadenacimiento=fechadenacimiento ,genero=genero,cedula=cedula ,telefono=telefono,correo=correo ,domicilio=domicilios)
        empleado=Empleado(id=1,sueldo=sueldo ,fechadeingreso=fechadeingreso, persona=persona)
        empleados.append(empleado)
        print(empleado.get_empleado())
        
        id= id + 1
        respuesta= input("quieres ingresar otro?: ")
        if respuesta== "no":
            break

    