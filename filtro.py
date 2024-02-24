# Librerias
import sys

# Funciones
def filtrar(diccionario, umbral):
    filtro = {k:v for k,v in diccionario.items() if v > umbral}
    output = ", ".join(filtro.keys())
    return print(f"Los productos mayores al umbral son: {output}")

def filtrar_menor(diccionario, umbral):
    filtro = {k:v for k,v in diccionario.items() if v < umbral}
    return print(f"Los productos menores al umbral son: {output}")

# Diccionario sobre el que trabajaremos
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
    }

# Se defina la cantidad de argumentos recibidos
n_argv = len(sys.argv) - 1

# Se valida la cantidad de argumentos, y la respectiva funcion a ejecutar
if n_argv == 1:
    filtrar(precios, int(sys.argv[1]))
elif n_argv == 2:
    if sys.argv[2] == "menor":
        filtrar_menor(precios, int(sys.argv[1]))
    else:
        print("Lo sentimos, no es una operación válida")
else:
    print("Cantidad de argumentos inválidos")
    
