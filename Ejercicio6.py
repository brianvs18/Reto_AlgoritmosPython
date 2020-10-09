# Realizar un algoritmo que lea un número por teclado. En caso de que ese número sea 0
# o menor que 0, se saldrá del programa imprimiendo antes un mensaje de error.
# Si es mayor que 0, se deberá calcular su cuadrado y la raiz cuadrada del mismo,
# visualizandoel numero que ha tecleado el usuario y su resultado
# (“Del numero X, su potencia es X y su raiz X” ).
# Para calcular la raiz cuadrada se puede usar la función interna RAIZ(X)  o con una potencia de 0,5

num1 = 0
pot = 0
raiz = 0

num1 = int(input("Ingrese un numero: "))

if num1 <= 0:
    print("E R R O R")
else: 
    pot = pow(num1, 2)
    raiz = num1**0.5
    print("Del numero "+ str(num1) +", su potencia es "+ str(pot) + ", y su raiz "+ str(raiz))