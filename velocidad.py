# Se inicializa la variable a utilizar
velocidad = [25, 12, 19, 16, 11, 11, 24, 1, 14, 14, 16, 10, 6, 23, 13, 25, 4, 19, 14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2, 14, 23, 19, 23, 9, 18, 20, 22, 14, 1, 10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5, 11, 10, 18, 10, 14, 5, 23, 20, 23, 21]

# Se define el promedio
promedio = sum(velocidad)/len(velocidad)

# Se inicializa la variable resultante
correas_lentas = []

# Ciclo for para filtrar la posicion de las velocidades mayores al promedio
for posicion, vel in enumerate(velocidad):
    if int(vel) > promedio:
        correas_lentas.append(posicion)

# Metodo de Python Comprehension
# correas_lentas = [posicion for posicion, vel in enumerate(velocidad) if vel > promedio]

# Se imprime resultado
print(correas_lentas)

