from collections import deque
#fifo,first in first out +
fila = deque([1,2])
fila.append(3)
fila.append(4)
fila.append(5)
fila.popleft()
fila.popleft() #poroleft eliminar el primer elemento a la izquierda
print(fila)

if not fila:
    print("fila vacia")
