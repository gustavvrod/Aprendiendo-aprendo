import tkinter as tk

def visual(window = tk.Tk(),n=0,texto):
    label = tk.Label(text=texto)
    label.pack()
    window.mainloop()


