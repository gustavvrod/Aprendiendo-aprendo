#def imc(masa=64, estatura=1.8):
#  imc=masa/(estatura**2)
#  return (float(imc))
#imc()

#def velocidad(distancia=89.17627504102676, tiempo=1664.2342885831808):
#  velocidad1=distancia/tiempo
#  velocidad2=(distancia/tiempo)*(1000 /1)*(1/3.600 )
#  resultado = 'La velocidad es ' + (str(velocidad1)) + " km/h o " + (str(velocidad2)) + " m/s"
#  return resultado
#velocidad()

#def xor(a=10, b=8):
#  xor=a<b
#  return xor
#xor()


#lat = -33.499188
#lon = -70.615126
#lat_domicilio = float(input("ingresa lat: "))
#lon_domicilio = float(lon)
#estoy_al_sur = lat_domicilio > lat 
#print(estoy_al_sur)



#print("Bienvenido a ... ")
#print("""
#                __  .__                          __   
#______ ___.__._/  |_|  |__   ____   ____   _____/  |_ 
#\____ <   |  |\   __\  |  \ /  _ \ /    \_/ __ \   __\
#|  |_> >___  | |  | |   Y  (  <_> )   |  \  ___/|  |  
#|   __// ____| |__| |___|  /\____/|___|  /\___  >__|  
#|__|   \/                \/            \/     \/      
#
#""")


nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

agno = int(input("Para preparar tu perfil, dime en que agno naciste. "))
edad = 2017-agno-1
print()

estatura = float(input("Cuentame mas de ti, para agregarlo a tu perfil. ¿Cuanto mides? Da­melo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

masa= float(input("Cuentame mas de ti, para agregarlo a tu perfil. ¿Cuanto pesas? Da­melo en kilogramos. "))
imc=(float(masa/(estatura**2)))

pais=input("Dinos en que pais vives?  ")
ciudad=input("En que ciudad?  ")

genero=input("Ingresa el genero con el cual te identificas principalmente.  ")

num_amigos = int(input("Muy bien. Finalmente, cuentame cuantos amigos tienes. "))

print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "agnos")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centi­metros", "imc: ", imc)
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la informacion. Esperamos que disfrutes con Mi Red")
print()

mensaje = input("Ahora vamos a publicar tu primer mensaje. ¿Que piensas hoy? ")
print()
print("--------------------------------------------------")
print(nombre, "dice:", mensaje)
print("--------------------------------------------------")
