import tkinter as tk
import controlusuario
from usuario import Usuario
from contrasena import Contrasena

class RegistraUsuario():
    def __init__(self,window):
        self.window=window        
        self.greeting = tk.Label(self.window, text="Administrador de empleado",fg="white",bg="black",height=10)
        self.greeting.pack()
        self.label_nombre = tk.Label(self.window, text="ingrese usuario a crear: ",fg="red",bg="white")
        self.label_nombre.pack()
        self.entry_nombre = tk.Entry(self.window)
        self.entry_nombre.pack()
        self.label_contrasena = tk.Label(self.window, text="ingrese contraseña a crear: ",fg="red",bg="white")
        self.label_contrasena.pack()
        self.entry_contrasena = tk.Entry(self.window)
        self.entry_contrasena.pack()
        self.label_correo = tk.Label(self.window, text="ingrese correo: ",fg="red",bg="white")
        self.label_correo.pack()
        self.entry_correo = tk.Entry(self.window)
        self.entry_correo.pack()
        self.button=tk.Button(self.window, text="CREAR",command=self.crear_usuario)
        self.button.pack()
        self.window.mainloop() 
        
    def crear_usuario(self):
        usuario=Usuario(nombre=self.entry_nombre.get(),contrasena=Contrasena(self.entry_contrasena.get()),correo=self.entry_correo.get())
        usuario.set_id(usuario.get_id())
        controlusuario.update(usuario)

    def Run(self):
        self.window.mainloop() 

if __name__ == "__main__":
    window=tk.Tk()
    registra=RegistraUsuario(window)
    registra.Run



