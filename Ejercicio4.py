#Algoritmo que lea tres números distintos y nos diga cual de ellos es el mayor (recuerda usar la estructura condicional Si y los operadores lógicos).

num1 = 0
num2 = 0
num3 = 0

num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))
num3 = int(input("Ingrese numero 3: "))

if num1 > num2 and num1 > num3:
    print("El numero mayor es: "+ str(num1))
elif num2 > num1 and num2 > num3:
    print("El numero mayor es: "+ str(num2))
elif num3 > num1 and num3 > num2:
    print("El numero mayor es: "+ str(num3))