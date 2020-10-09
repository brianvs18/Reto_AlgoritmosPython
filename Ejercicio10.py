# Modificar el algoritmo anterior, de forma que si se teclea un cero, se vuelva a pedir el número por teclado
# (así hasta que se teclee un número mayor que cero) (recuerda la estructura mientras).

num = 0

while True:
    num = int(input("Ingrese un numero: "))
    if num != 0:
        break