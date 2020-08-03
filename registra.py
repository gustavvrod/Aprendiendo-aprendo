import tkinter as tk
import controlusuario
from claseregistrausuario import RegistraUsuario
from usuario import Usuario


window=tk.Tk()
usuarios=controlusuario.update() 
if usuario == usuarios:
    RegistraUsuario(window,usuario())
    
window.mainloop()
