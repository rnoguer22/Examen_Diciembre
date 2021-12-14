def minion_game(string):
    # Establecemos los puntos de ambos jugadores como 0
    Puntos_Kevin = 0
    Puntos_Stuart = 0
    # Elaboramos un bucle que nos calculara los puntos de cada jugador
    for i in range(6):
        if palabra[i] not in vocales:   # Si la letra no es una vocal, calcula los puntos de Stuart
            Puntos_Stuart += 6 - i
        else:
            Puntos_Kevin += 6 - i   # Si la letra es una vocal, calcula los puntos de Kevin
    return [Puntos_Kevin, Puntos_Stuart]

if __name__ == '__main__':
    palabra = "Banana"
    vocales = ["a", "e", "i", "o", "u"]   # Definimos las vocales en una lista
