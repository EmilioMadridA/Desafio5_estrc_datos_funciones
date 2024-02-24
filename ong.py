# Librerias
import math

# Se define funcion con "**kwargs" para recibir multiples argumentos
def calcular(**kwargs):
    # Se evalua la clave y el valor del argumento
    for clave, valor in kwargs.items():
        # Se evalua si la operacion es factorial o productorial
        if "fact_" in clave:
            factorial = math.factorial(valor)
            print(f"El factorial de {valor} es {factorial}")
        elif "prod_" in clave:
            productorio = 1
            for elemento in valor:
                productorio *= elemento
            print(f"La productoria de {valor} es {productorio}")
        else:
            print(f"La operacion de {clave} = {valor} no es válida")

# Se llama a la funcion con varias variables
calcular(fact_1 = 5, prod_1 = [4,6,7,4,3], fact_2 = 6)
