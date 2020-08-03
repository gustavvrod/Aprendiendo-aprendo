import tkinter as tk
import controlusuario
from usuario import Usuario
from contrasena import Contrasena

class EliminaRowUsuario():
    def __init__(self, window, usuario, row):
        self.row= row
        self.window = window
        self.usuario=usuario
        self.label_datos=tk.Label(self.window,text=self.usuario.get_id())
        self.label_datos.grid(row=self.row, column=1)
        self.label_nombre=tk.Label(self.window,text=self.usuario.get_nombre())
        self.label_nombre.grid(row=self.row, column=0)
        self.label_contrasena=tk.Label(self.window,text=self.usuario.contrasena.get_contrasena())
        self.label_contrasena.grid(row=self.row, column=2)
        self.label_correo=tk.Label(self.window,text=self.usuario.get_correo())
        self.label_correo.grid(row=self.row, column=3)
        self.button=tk.Button(self.window,text="Eliminar", command= self.elimina_usuario)
        self.button.grid(row=self.row, column=4)
        


    def elimina_usuario(self):
        controlusuario.delete(int(self.usuario.get_id()))          




