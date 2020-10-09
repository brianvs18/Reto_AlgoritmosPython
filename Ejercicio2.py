#Algoritmo que lea dos números, calculando y escribiendo el valor de su suma, resta, producto y división

num1 = 0
num2 = 0
suma = 0
resta = 0
producto = 0
division = 0

num1 = float(input("Ingrese número 1: "))
num2 = float(input("Ingrese número 2: "))
suma = num1 + num2
resta = num1 - num2
producto = num1 * num2
division = num1 / num2
print("Suma: "+ str(suma))
print("Resta: "+ str(resta))
print("Multiplicacion: "+ str(producto))
print("Division: "+ str(division))