import random

def printeartablero(tableroajedrez):
    contador_indice = 0
    for tableroajedrez[contador_indice] in tableroajedrez:
        print(tableroajedrez[contador_indice])
        contador_indice += 1
    print("\n")   # Salto de linea para los futuros tableros

def movimiento(fila, columna):
    if fila == 0:
            tableroajedrez[fila+1][columna] = tableroajedrez[fila][columna]
            tableroajedrez[fila][columna] = ' '
    elif fila == 1:
        if tableroajedrez[fila+1][columna] != ' ':
            tableroajedrez[fila-1][columna] = tableroajedrez[fila][columna]
            tableroajedrez[fila][columna] = ' '
        else:
            tableroajedrez[fila+1][columna] = tableroajedrez[fila][columna]
            tableroajedrez[fila][columna] = ' '
    elif fila == 2:
        tableroajedrez[fila-1][columna] = tableroajedrez[fila][columna]
        tableroajedrez[fila][columna] = ' '

def cambio(fila, columna):
    if  fila == 0:
        fila += 1
    elif fila == 1:
        if tableroajedrez[fila+1][columna] != ' ':
            fila -= 1
        else:
            fila += 1
    elif fila == 2:
        fila -= 1
    return fila   # Devuelve la nueva posicion de la ficha

def encerrada(fila, columna):
    if fila == 0 and tableroajedrez[fila+1][columna] != ' ':
        error = True   # Esta condicion se cumple si abajo hay una ficha
    elif fila == 1:
        if tableroajedrez[fila+1][columna] != ' ' and tableroajedrez[fila-1][columna] != ' ':
            error = True   # Esta condicion se cumple si arriba y abajo hay fichas
        else:
            error = False
    elif fila == 2 and tableroajedrez[fila-1][columna] != ' ':
            error = True   # Esta condicion se cumple si arriba hay una ficha
    else:
        error = False
    return error   # Devuelve el boolean asociado a error, para saber si una ficha esta encerrada o no

# Bucle infinito para la creacion de cada jugada del ajedrez
while True:
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

    printeartablero(tableroajedrez)   # Printamos el primer tablero, con las piezas en una posicion random

    errorx = encerrada(x, 0)
    errory = encerrada(y, 1)
    errorz = encerrada(z, 2)
    errora = encerrada(a, 0)
    errorb = encerrada(b, 1)
    errorc = encerrada(c, 2)

    if errorx and errory and errorz == True:   # Esto significa que en el primer tablero las piezas negras obstrullen a las blancas, por lo que no se podrian mover
        print("El jugador blanco no se puede mover, volvemos a crear el tablero")
    elif errora and errorb and errorc == True:   # Y viceversa
        print("El jugador negro no se puede mover, volvemos a crear el tablero")
    else:
        break

turno = random.randint(0, 1)
while True:
    if turno == 1:
        if errorx == False and errora == False:
            movimiento(x, 0)
            x = cambio(x, 0)
            errora = encerrada(a, 0)
        elif errory == False and errorb == False:
            movimiento(y, 1)
            y = cambio(y, 1)
            errorb = encerrada(b, 1)
        elif errorz == False and errorc == False:
            movimiento(z, 2)
            z = cambio(z, 2)
            errorc = encerrada(c, 2)
        elif errorx == False:
            movimiento(x, 0)
            x = cambio(x, 0)
            errora = encerrada(a, 0)
        elif errory == False:
            movimiento(y, 1)
            y = cambio(y, 1)
            errorb = encerrada(b, 1)
        elif errorz == False:
            movimiento(z, 2)
            z = cambio(z, 2)
            errorc = encerrada(c, 2)
        else:
            break
        turno = 0
    elif turno == 0:
        if errora == False and errorx == False:
            movimiento(a, 0)
            a = cambio(a, 0)
            errorx = encerrada(x, 0)
        elif errorb == False and errory == False:
            movimiento(b, 1)
            b = cambio(b, 1)
            errory = encerrada(y, 1)
        elif errorc == False and errorz == False:
            movimiento(c, 2)
            c = cambio(c, 2)
            errorz = encerrada(z, 2)
        elif errora == False:
            movimiento(a, 0)
            a = cambio(a, 0)
            errorx = encerrada(x, 0)
        elif errorb == False:
            movimiento(b, 1)
            b = cambio(b, 1)
            errory = encerrada(y, 1)
        elif errorc == False:
            movimiento(c, 2)
            c = cambio(c, 2)
            errorc = encerrada(z, 2)
        else:
            break
        turno = 1
    printeartablero(tableroajedrez)
if errorx and errory and errorz == True:
    print("Ha ganado el jugador negro, ya que es imposible que el jugador blanco se mueva")
elif errora and errorb and errorc == True:
    print("Ha ganado el jugador blanco, ya que el jugador negro no se puede mover")