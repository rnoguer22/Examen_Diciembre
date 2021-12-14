def minion_game(palabra):
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

def elegir_palabra():   # Definimos una funcion para elegir la palabra que queramos
    while True:
        palabrita = input("Introduzca la palabra: ")
        if palabrita == str(palabrita):   # De esta manera nos aseguramos que el usuario introduce una palabra y no otra cosa
            return palabrita
            break
        else:
            print ("Introduzca una palabra, no me trolees por favor")

if __name__ == '__main__':
    palabra = elegir_palabra()
    vocales = ["a", "e", "i", "o", "u"]   # Definimos las vocales en una lista
    resultado = minion_game(palabra)
    print ("Los puntos de Kevin son {} y los de Stuart son {}".format(resultado[0], resultado[1]))