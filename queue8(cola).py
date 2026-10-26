
from collections import deque
import time


cola_reproduccion=deque()
#agregar elementos de reproduccion
cola_reproduccion.append("1.- Mochila azul")
cola_reproduccion.append("2.- Aerolinea carrillo")
cola_reproduccion.append("3.- La calabaza")
#mostrar las canciones en espera
print("canciones en espera:")
for cancion in cola_reproduccion:
    print("_",cancion)
    print("iniciando reproduccion")
    #desencolar
    while cola_reproduccion:
        cancion_actual=cola_reproduccion.popleft()
        print(f"Sonando ahora:{cancion_actual}")
        time.sleep(1) #simula la duracion
        print(f"finalizo:{cancion_actual}")
        #muestra cuantas canciones quedan en la cola
        print(f"quedan{len(cola_reproduccion)}canciones en la cola")
        print("la cola de reproduccion ha finalizado")