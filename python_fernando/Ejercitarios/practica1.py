# Inicializar una lista vacía para almacenar las notas
notas = []

# Solicitar al usuario que ingrese tres notas
for i in range(3):
    while True:
        try:
            # Pedir al usuario que ingrese una nota
            nota = float(input(f"Ingrese la nota {i + 1}: "))
            # Verificar que la nota esté en el rango de 0 a 5
            if 0 <= nota <= 5:
                # Agregar la nota a la lista
                notas.append(nota)
                break
            else:
                print("La nota debe estar entre 0 y 5. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

# Calcular el promedio
promedio = sum(notas) / len(notas)

# Determinar si está aprobado o reprobado
estado = "APROBADO" if promedio > 1.7 else "REPROBADO"

# Mostrar los resultados
print(f"\nLas notas ingresadas son: {notas}")
print(f"Promedio: {promedio:.2f}")
print(f"Estado: {estado}")
