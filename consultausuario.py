import tkinter as tk
import controlusuario
from displayrowusuarios import DisplayRowUsuario
from usuario import Usuario

class ConsultaUsuario():
    def __init__(self,window):
        """Consulta Usuario Toma Un Parametro Window De Tkinter."""
        self.window=window
        self.greeting = tk.Label(self.window,text="Display Usuarios",fg="white",bg="black",height=10)
        self.greeting.grid(row=0)
        self.usuarios= controlusuario.retrieve()
        for usuario in self.usuarios:
            DisplayRowUsuario(self.window,usuario,self.usuarios.index(usuario)+1)
        self.window.mainloop()
    
if __name__ == "__main__":
    window = tk.Tk()
    consulta_usuario=ConsultaUsuario(window)