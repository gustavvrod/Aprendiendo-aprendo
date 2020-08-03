<<<<<<< HEAD
import random
import tkinter as tk

n = 0
ns = int(random.randint(0, 100))
contador = 10
#print(ns)

window = tk.Tk()
greeting = tk.Label(text="ADIVINA EL NÚMERO",fg="blue",bg="black",width=20,height=10)
greeting.pack()
label = tk.Label(text="Ingresar numero 0 a 100:",fg="red",bg="white")
label.pack()
entry = tk.Entry()
entry.pack()
    
def restart():
    global ns
    global contador
    contador = 10
    ns=random.randint(0, 100)
    label["text"]= "Ingresar numero 0 a 100:"
    button["state"]="active"
    button2["state"]="disabled"

button2=tk.Button(text="Reiniciar",command=restart,state= "disabled")
button2.pack()
    
def retrieve_input():
    global contador
    if entry.get().isdecimal():
        n = int(entry.get())
        if n == ns:
            label['text'] = "Ganaste!"
            button["state"]="disabled"
            button2["state"]="active"
        if n < ns:
            label['text'] = "Es un numero mayor."
        if n > ns:
            label['text'] = "Es un numero menor."
        if contador ==0: 
            label['text'] = "perdiste"
            button["state"]="disabled"
            button2["state"]="active"
        contador=contador-1

button=tk.Button(text="Validar",command=retrieve_input)
button.pack()   
  
window.mainloop()
=======
import random
import tkinter as tk

n = 0
ns = int(random.randint(0, 100))
contador = 10
#print(ns)

window = tk.Tk()
greeting = tk.Label(text="ADIVINA EL NÚMERO",fg="blue",bg="black",width=20,height=10)
greeting.pack()
label = tk.Label(text="Ingresar numero 0 a 100:",fg="red",bg="white")
label.pack()
entry = tk.Entry()
entry.pack()
    
def restart():
    global ns
    global contador
    contador = 10
    ns=random.randint(0, 100)
    label["text"]= "Ingresar numero 0 a 100:"
    button["state"]="active"
    button2["state"]="disabled"

button2=tk.Button(text="Reiniciar",command=restart,state= "disabled")
button2.pack()
    
def retrieve_input():
    global contador
    if entry.get().isdecimal():
        n = int(entry.get())
        if n == ns:
            label['text'] = "Ganaste!"
            button["state"]="disabled"
            button2["state"]="active"
        if n < ns:
            label['text'] = "Es un numero mayor."
        if n > ns:
            label['text'] = "Es un numero menor."
        if contador ==0: 
            label['text'] = "perdiste"
            button["state"]="disabled"
            button2["state"]="active"
        contador=contador-1

button=tk.Button(text="Validar",command=retrieve_input)
button.pack()   
  
window.mainloop()
>>>>>>> 1c9b3fe7fa8ff626d39cf70b9be4a6d30c839497
