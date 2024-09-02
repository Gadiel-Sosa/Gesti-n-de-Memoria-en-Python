# Código para manejo de memoria estática (arreglos fijos)
calificaciones = [0] * 5

for i in range(5):
    calificaciones[i] = int(input("Captura la calificación: "))
    print(f"{calificaciones[i]} calificación")

# Código para manejo de memoria dinámica (listas dinámicas)
frutas = []

frutas.append("Mango")
frutas.append("Manzana")
frutas.append("Banana")
frutas.append("Uvas")

print(frutas)

# Eliminando elementos por índice
del frutas[0]  # Elimina Mango
del frutas[1]  # Elimina Banana

frutas.append("Sandia")

print(frutas)
