# Desarrollar un algoritmo que nos calcule el cuadrado de los 9 primeros números naturales
# (recuerda la estructura desde-hasta)

num = 0

for i in range (0,9):
    i+=1
    num = pow(i,2)
    print(num)