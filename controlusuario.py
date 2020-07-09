import json
from usuario import Usuario
from contrasena import Contrasena
import os


archivo= "Usuarios"
cw=os.getcwd()


def create():
    f = open(archivo + ".json", "w")
    f.write("[]")
    f.close()

def retrieve():
    with open(archivo +'.json',"r") as json_file:
        usuarios_data = json.loads(json_file.read())
        usuarios=[]
        for data in usuarios_data:
            usuario=Usuario(nombre=data["nombre"],contrasena=Contrasena(data["contrasena"]["contrasena"]),correo= data["correo"])
            usuario.set_id(data["id"])
            usuarios.append(usuario)
        return usuarios
        

def retrieve_by_id(id:int):
    usuarios=retrieve()
    for usuario in usuarios:
        if usuario.get_id()==id:
            return usuario

def update(usuario: Usuario):
    users=retrieve()
    n=len(users)
    id=usuario.get_id()
    if n > 0:        
        if id > n or id == 0:
            id=n+1
            usuario.set_id(id)
            users.append(usuario)
        else:
            users[id-1]=usuario
    else:
        usuario.set_id(1)
        users.append(usuario)
    users_data=[]
    for user in users:
        users_data.append(user.__dict__)
    for user in users_data:
        user["contrasena"]=user["contrasena"].__dict__
    with open(archivo +'.json', 'w') as outfile:
        data=json.dumps(users_data,sort_keys=False,indent=4)
        outfile.write(data)


def delete(usuario, id:int):
    users=retrieve()
    n=len(users)
    if n > 0: 
        for user in users:
            if user.get_id()==usuario.get_id():
                user = usuario
            else:
                usuario.set_id(n+1)
                users.append(usuario)
                break
    else:
        usuario.set_id(1)
        users.append(usuario)
    users_data=[]
    for user in users:
        users_data.append(user.__dict__)
    for user in users_data:
        user["contrasena"]=user["contrasena"].__dict__
    with open(archivo +'.json', 'w') as outfile:
        data=json.dumps(users_data,sort_keys=False,indent=4)
        outfile.write(data)
    

if __name__ == "__main__":
    respuesta=(int(input("1:create,2:retrieve,3:delete;4:update")))
    if respuesta==1:
       create()
    

