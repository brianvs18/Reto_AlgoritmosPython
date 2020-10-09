#Diseñar un algoritmo que pida por teclado tres números; si el primero es negativo,
#debe imprimir el producto de los tres y si no lo es, imprimirá la suma

num1 = 0
num2 = 0
num3 = 0

num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))
num3 = int(input("Ingrese numero 3: "))

if num1 < 0:
    result = num1 * num2 * num3
    print("Primer numero negativo, producto: "+ str(result))
elif num1 > 0:
    result = num1 + num2 + num3
    print("Primer numero positivo, suma: "+ str(result))
