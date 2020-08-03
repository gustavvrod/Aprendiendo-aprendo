import tkinter as tk
import controlusuario
from usuario import Usuario
from contrasena import Contrasena


def editar_usuario(usuario:Usuario,window):
    print("funcion: ")
    print(usuario)
    greeting = tk.Label(window,text="Editor de usuario",fg="white",bg="black",height=10)
    greeting.grid(row=0)
    r=1
    label_id=tk.Label(window, text=usuario.get_id())
    label_id.grid(row=r, column=0)
    entry_nombre=tk.Entry(window)
    entry_nombre.insert(0,usuario.get_nombre())
    entry_nombre.grid(row=r, column=1)
    entry_contrasena=tk.Entry(window)
    entry_contrasena.insert(0,usuario.get_contrasena().get_contrasena())
    entry_contrasena.grid(row=r, column=2)
    entry_correo=tk.Entry(window)
    entry_correo.insert(0,usuario.get_correo())
    entry_correo.grid(row=r, column=3)
    button=tk.Button(window,text="Guardar")
    button.grid(row=r, column=4)
    
