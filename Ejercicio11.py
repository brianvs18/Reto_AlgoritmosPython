# Algoritmo que nos diga si una persona puede acceder a cursar un ciclo formativo de grado superior o no.
# Para acceder a un grado superior, si se tiene un titulo de bachiller, en caso de no tenerlo,
# se puede acceder si hemos superado una prueba de acceso.

leer = ""

leer = input("¿Tiene titulo de bachiller?: ")
if leer == "si":
    print("Puede acceder al ciclo formativo")
elif leer == "no":
    print("No puede acceder al ciclo formativo")
    print("Para acceder debe haber superado la prueba de acceso")
    leer = input("¿Superó la prueba de acceso?: ")
    if leer == "si":
        print("Puede acceder al ciclo formativo")
    else:
        print("No puede acceder al ciclo formativo")