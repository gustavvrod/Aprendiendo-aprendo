import random

n = 0
ns = int(random.randint(0, 100))
#print(ns)



while True:
    n= int(input ("introduce numero entre 0 y 100: "))
    if n == ns:
        input("Ganaste")
        break
    if n < ns:
        print("Es un numero mayor.")
    if n > ns:
        print("Es un numero menor.")

    

    