#Algoritmo que lea dos números y nos diga cual de ellos es mayor o bien si son iguales (recuerda usar la estructura condicional SI)

num1 = 0
num2 = 0

num1 = int(input("Ingrese el numero 1: "))
num2 = int(input("Ingrese el numero 2: "))

if num1 > num2:
    print("El numero mayor es: "+ str(num1))
elif num2 > num1:
    print("El numero mayor es: "+ str(num2))
elif num1 == num2:
    print("Los numeros tienen el mismo valor")