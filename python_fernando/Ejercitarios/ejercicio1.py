"""leer tres notas por teclado y cargar en una lista.
Calcular el promedio si está aprobado o re´robado.
Si promedio > 1.7 = aprobado sino reprobado"""

notas = [] #declara una variable lista 
totalNotas = 0

#cargar la lista
for x in range(3):
    nota = 0
    while nota < 1 or nota > 5:
        nota = int(input(f"Ingrese la nota {x + 1}: "))
    notas.append(nota)
    totalNotas = totalNotas + nota
        
    #calcular el promedio y si esta aprobado o reprobado
    promedio = totalNotas / 3
    
    #Determinar si está aprobado o reprobado
#estado = "APROBADO" 
if promedio > 1.7: 
    print("Aprobado")2
else:
    print("REPROBADO")
print(f"El promedio de las notas: {notas} es {promedio:.2f}")
#print(f"Estado: {estado}")
    
    # Mostrar los resultados
#print(f"\nLas notas ingresadas son: {notas}")
#print(f"Promedio: {promedio:.2f}")

