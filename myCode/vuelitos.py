import random
import numpy as np

print("Vuelitos")
print("1. Crear Vuelo ingresando (debe validar la cantidad de pasajeros sea positiva y los destinos sean Paris,")
print("Barcelona o Hamburgo, se debe cargar la semana completa")
print("2. Crear vuelo aleatorio")
print("3. Mostrar información (mostrará la información)")
print("4. Cantidad")
print("5. Total Ganado (validar destino)")
print("6. Sobre cupo (si no se crea arreglo, dar un mensaje adecuado)")
print("7. Salir.")

pax = 195000

fligths = np.array([]) 

def paxRandom():
    result = random.randint(150, 500)
    return result

def cityRandom():
    result = random.randint(1, 3)
    if result == 1:
        return "barcelona"
    if result == 2:
        return "hamburgo"
    if result == 3:
        return "paris"


def isOvercrowded(flight): return True if flight > 300 else False

def newFligth (dest1, dest2, dest3, dest4, dest5, dest6, dest7):
    result = np.array([])
