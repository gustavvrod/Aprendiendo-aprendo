import tkinter as tk
from consultausuario import ConsultaUsuario
from claseregistrausuario import RegistraUsuario


class VentanaMain():
    def __init__(self):
        self.window1=tk.Tk()
        self.greeting = tk.Label(text="Ingresa usuario",fg="white",bg="black",height=10)
        self.greeting.pack()
        self.button=tk.Button(text="CREAR",command= self.RegistraUsuario)
        self.button.pack()
        self.greeting = tk.Label(text="Consulta usuario",fg="white",bg="black",height=10)
        self.greeting.pack()
        self.button=tk.Button(text="CONSULTA", command= self.ConsultaUsuario)
        self.button.pack()


    def RegistraUsuario(self):
        window2=tk.Toplevel(self.window1)
        self.registra=RegistraUsuario(window2)

    def ConsultaUsuario(self):
        window2=tk.Toplevel(self.window1)
        self.consulta=ConsultaUsuario(window2)
    
    def Run(self):
        self.window1.mainloop()


if __name__ == "__main__":
    main=VentanaMain()
    main.Run()
