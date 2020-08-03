import tkinter as tk
import controlusuario
from usuario import Usuario
from contrasena import Contrasena


window = tk.Tk()
greeting = tk.Label(text="Administrador de empleado",fg="white",bg="black",height=10)
greeting.pack()
label_nombre = tk.Label(text="ingrese usuario a crear: ",fg="red",bg="white")
label_nombre.pack()
entry_nombre = tk.Entry()
entry_nombre.pack()

label_contrasena = tk.Label(text="ingrese contraseña a crear: ",fg="red",bg="white")
label_contrasena.pack()
entry_contrasena = tk.Entry()
entry_contrasena.pack()

label_correo = tk.Label(text="ingrese correo: ",fg="red",bg="white")
label_correo.pack()
entry_correo = tk.Entry()
entry_correo.pack()


def crear_usuario():
    global entry_nombre
    global entry_contrasena
    global entry_correo
    nombre=entry_nombre.get()
    contrasena=entry_contrasena.get()
    correo=entry_correo.get()
    usuario=Usuario(nombre=nombre, contrasena=Contrasena(contrasena), correo=correo)
    controlusuario.update(usuario)


button=tk.Button(text="CREAR",command=crear_usuario)
button.pack()   

window.mainloop()
