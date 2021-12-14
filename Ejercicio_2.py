import random

# Creamos el tablero vacio
tableroajedrez = [
[' ', ' ', ' '], 
[' ', ' ', ' '],
[' ', ' ', ' '], 
]

# Creamos variables aleatorias que utilizaremos proximamente
x = random.randint(0,2)
y = random.randint(0,2)
z = random.randint(0,2)
a = random.randint(0,2)
b = random.randint(0,2)
c = random.randint(0,2)

while x == a:
    a = random.randint(0,2)
while y == b:
    b = random.randint(0,2)
while z == c:
    c = random.randint(0,2)

# Establecemos la posicion de las piezas
tableroajedrez[x][0] = chr(0x2656)
tableroajedrez[y][1] = chr(0x2656)
tableroajedrez[z][2] = chr(0x2656)
tableroajedrez[a][0] = chr(0x265C)
tableroajedrez[b][1] = chr(0x265C)
tableroajedrez[c][2] = chr(0x265C)