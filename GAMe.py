import random
import tkinter as tk

n = 0
ns = int(random.randint(0, 100))
#print(ns)

window = tk.Tk()
greeting = tk.Label(text="ADIVINA EL NÚMERO",fg="white",bg="black",width=20,height=10)
greeting.pack()
label = tk.Label(text="Ingresar numero 0 a 100:",fg="red",bg="white")
label.pack()
entry = tk.Entry()
entry.pack()




def retrieve_input():
    if entry.get().isdecimal():
        n = int(entry.get())
        if n == ns:
            label['text'] = "Ganaste!" 
            deshabilitar()
        if n < ns:
            label['text'] = "Es un numero mayor."
        if n > ns:
            label['text'] = "Es un numero menor."

      
button=tk.Button(text="Validar",command=retrieve_input)
button.pack()   
def deshabilitar():
    entry["state"] = "disabled"
    button["state"] = "disabled"   
window.mainloop()



    

    