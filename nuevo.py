import tkinter as tk
from tkinter import ttk
import controlusuario
from usuario import Usuario
from contrasena import Contrasena



class Displayusuarios(ttk.Frame):
    def __init__(self, main_window, label_datos:[]):
        self.label_datos=datos 
        super().__init__(main_window)
        main_window.title("Display usuarios")        
        self.label_datos = ttk.Label(self, text="¡Hola, mundo!")
        self.label_datos.grid(row=0, column=1)
        self.label_datos = ttk.Label(self, text="¡Hola, mundo!")
        self.label_datos.grid(row=1, column=0)
        self.label_datos = ttk.Label(self, text="...desde Tkinter!")
        self.label_datos.pack()

window = tk.Tk()
greeting = tk.Label(text=" Display Usuarios ",fg="white",bg="black",height=10)
greeting.pack()
window.mainloop()