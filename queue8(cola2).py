
from collections import deque
import time
cola=deque()
#agregar elementos 
cola.append("cliente 1")
cola.append("cliente 2")
cola.append("cliente 3")
#sacar el primer elemento atendido (desencolar)
atendido=cola.popleft()
#mostrar resultados
print("atendido", atendido)
print("cola restante", cola)
