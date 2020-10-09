# Una tienda ofrece un descuento del 15% sobre el total de la compra durante el mes de octubre.
# Dado un mes y un importe, calcular cuál es la cantidad que se debe cobrar al cliente

omp = 0

comp = int(input("Ingrese el valor de compra: "))
mes = int(input("Ingrese el numero del mes de compra: "))

if mes == 10:
    des = comp * 0.15
    total = comp - des
    print("Descuento: "+str(des))
    print("Total a pagar: "+str(total))
else:
    print("Total a pagar: "+str(comp))