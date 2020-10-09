# Realizar un algoritmo que dado un número entero, visualice en pantalla si es par o impar.
# En el caso de ser 0, debe visualizar “el número no es par ni impar”
# (para que un numero sea par, se debe dividir entre dos y que su resto sea 0)

num = 0

num = int(input("Ingrese un numero: "))
res = num%2
if num == 0:
    print("El numero no es par ni impar")
elif res == 0:
    print("El numero es par")
else:
    print("El numero es impar")