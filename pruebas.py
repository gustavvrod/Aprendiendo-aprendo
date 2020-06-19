import tkinter as tk
window = tk.Tk()
label = tk.Label(text="Adivina numero")
greeting = tk.Label(text="Ingresar numero:")
entry = tk.Entry()
greeting.pack()
label.pack()
entry.pack()
n=entry.get()



window.mainloop()

