import tkinter as tk
import controlusuario
from displayrowusuarios import DisplayRowUsuario
from usuario import Usuario


window = tk.Tk()
greeting = tk.Label(text="Display Usuarios",fg="white",bg="black",height=10)
greeting.grid(row=0)
usuarios= controlusuario.retrieve()
for usuario in usuarios:
    DisplayRowUsuario(window,usuario,usuarios.index(usuario)+1)

window.mainloop()
