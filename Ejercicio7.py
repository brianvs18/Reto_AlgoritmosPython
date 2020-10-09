# Un colegio desea saber qué porcentaje de niños y qué porcentaje de niñas
# hay en el curso actual. Diseñar un algoritmo para este propósito
# (recuerda que para calcular el porcentaje puedes hacer una regla de 3)

ninos = 0
ninas = 0

ninos = int(input("Ingrese la cantidad de niños: "))
ninas = int(input("Ingrese la cantidad de niñas: "))
total = ninos + ninas
res1 = (ninos*100)/total
res2 = (ninas*100)/total
print("El porcentaje de niños es: "+str(res1)+"%")
print("El porcentaje de niñas es: "+str(res2)+"%")