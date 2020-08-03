<<<<<<< HEAD
import tkinter as tk
import controlusuario
from usuario import Usuario
from contrasena import Contrasena

class DisplayRowUsuario():
    def __init__(self, window, usuario, row):
        self.row= row
        self.window = window
        self.usuario= usuario
        self.label_datos = tk.Label(self.window,text=self.usuario.get_id())
        self.label_datos.grid(row = self.row, column=1)
        self.label_nombre = tk.Label(self.window,text=self.usuario.get_nombre())
        self.label_nombre.grid(row = self.row, column=0)
        self.label_contrasena = tk.Label(self.window,text=self.usuario.contrasena.get_contrasena())
        self.label_contrasena.grid(row = self.row, column=2)
        self.label_correo = tk.Label(self.window,text = self.usuario.get_correo())
        self.label_correo.grid(row = self.row, column=3)
        self.button = tk.Button(self.window,text="Editar", command= self.editar_usuario)
        self.button.grid(row = self.row, column=4)
     

        
    def editar_usuario(self):
        window2=tk.Toplevel(self.window)
        greeting = tk.Label(window2,text="Editor de usuario",fg="white",bg="black",height=10)
        greeting.grid(row=0)
        r=1
        label_id=tk.Label(window2, text=self.usuario.get_id())
        label_id.grid(row=r, column=0)
        self.entry_nombre=tk.Entry(window2)
        self.entry_nombre.insert(0,self.usuario.get_nombre())
        self.entry_nombre.grid(row=r, column=1)
        self.entry_contrasena=tk.Entry(window2)
        self.entry_contrasena.insert(0,self.usuario.get_contrasena().get_contrasena())
        self.entry_contrasena.grid(row=r, column=2)
        self.entry_correo=tk.Entry(window2)
        self.entry_correo.insert(0,self.usuario.get_correo())
        self.entry_correo.grid(row=r, column=3)
        self.check_var= tk.BooleanVar()
        self.check_activo = tk.Checkbutton(window2,text="Activo",variable=self.check_var)
        if self.usuario.get_activo():
            self.check_activo.select()
        self.check_activo.grid(row=r, column=4)
        self.button=tk.Button(window2, text="Guardar", command= self.update_usuario)
        self.button.grid(row=r, column=5)

    def update_usuario(self):
        usuario=Usuario(nombre=self.entry_nombre.get(),contrasena=Contrasena(self.entry_contrasena.get()),correo=self.entry_correo.get())
        usuario.set_id(self.usuario.get_id())
        if not self.check_var.get():
            usuario.set_activo(False)
        controlusuario.update(usuario)            




=======
import tkinter as tk
import controlusuario
from usuario import Usuario
from contrasena import Contrasena

class DisplayRowUsuario():
    def __init__(self, window, usuario, row):
        self.row= row
        self.window = window
        self.usuario=usuario
        self.label_datos=tk.Label(text=self.usuario.get_id())
        self.label_datos.grid(row=self.row, column=1)
        self.label_nombre=tk.Label(text=self.usuario.get_nombre())
        self.label_nombre.grid(row=self.row, column=0)
        self.label_contrasena=tk.Label(text=self.usuario.contrasena.get_contrasena())
        self.label_contrasena.grid(row=self.row, column=2)
        self.label_correo=tk.Label(text=self.usuario.get_correo())
        self.label_correo.grid(row=self.row, column=3)
        self.button=tk.Button(text="Editar", command= self.editar_usuario)
        self.button.grid(row=self.row, column=4)
        

        
    def editar_usuario(self):
        window2=tk.Toplevel(self.window)
        greeting = tk.Label(window2,text="Editor de usuario",fg="white",bg="black",height=10)
        greeting.grid(row=0)
        r=1
        label_id=tk.Label(window2, text=self.usuario.get_id())
        label_id.grid(row=r, column=0)
        self.entry_nombre=tk.Entry(window2)
        self.entry_nombre.insert(0,self.usuario.get_nombre())
        self.entry_nombre.grid(row=r, column=1)
        self.entry_contrasena=tk.Entry(window2)
        self.entry_contrasena.insert(0,self.usuario.get_contrasena().get_contrasena())
        self.entry_contrasena.grid(row=r, column=2)
        self.entry_correo=tk.Entry(window2)
        self.entry_correo.insert(0,self.usuario.get_correo())
        self.entry_correo.grid(row=r, column=3)
        button=tk.Button(window2,text="Guardar", command= self.update_usuario)
        button.grid(row=r, column=4)

    def update_usuario(self):
        usuario=Usuario(nombre=self.entry_nombre.get(),contrasena=Contrasena(self.entry_contrasena.get()),correo=self.entry_correo.get())
        usuario.set_id(self.usuario.get_id())
        controlusuario.update(usuario)            




>>>>>>> 1c9b3fe7fa8ff626d39cf70b9be4a6d30c839497
