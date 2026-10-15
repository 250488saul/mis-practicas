historial_navegacion=[]
historial_navegacion.append("google.com")
historial_navegacion.append("youtube.com")
historial_navegacion.append("wikipedia.org")
print("historial_cargado",historial_navegacion)

pagina_actual=historial_navegacion[-1]
print("pagina actual en pantalla;", pagina_actual)

#operacion de desapilar(POP)
pagina_cerrada=historial_navegacion.pop()
print("saliendo de ",pagina_cerrada)
print("historial despues de presionar 'Atras':", historial_navegacion)

#Tamaño de pila
total_paginas=len(historial_navegacion)
print("paginas previas guardadas:", total_paginas)

#operacion vacia (empty)
sin_paginas=len(historial_navegacion)==0
print("¿El historial esta vacio?", sin_paginas)
