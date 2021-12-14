from colorama import Fore, init
init(autoreset=False)   # De esta manera la salida al ejecutar el codigo sera entera en amarillo

def elegir_palabra():   # Definimos una funcion para elegir la palabra que queramos
    while True:
        palabrita = input(Fore.YELLOW + "Introduzca la palabra: ")
        if palabrita == str(palabrita):   # De esta manera nos aseguramos que el usuario introduce una palabra y no otra cosa
            return palabrita
        else:
            print ("Introduzca una palabra, no me trolees por favor")

def minion_game():
    # Establecemos los puntos de ambos jugadores como 0
    Puntos_Kevin = 0
    Puntos_Stuart = 0
    # Elaboramos un bucle que nos calculara los puntos de cada jugador
    for i in range(len(palabra)):
        if palabra[i] not in vocales:   # Si la letra no es una vocal, calcula los puntos de Stuart
            Puntos_Stuart += len(palabra) - i
        else:
            Puntos_Kevin += len(palabra) - i   # Si la letra es una vocal, calcula los puntos de Kevin
    return [Puntos_Kevin, Puntos_Stuart]

def ganador(resultado):   # Esta funcion nos va a decir el ganador
    if resultado[0] > resultado[1]:
        print ("Ha ganado Kevin")
        print ("Con un total de {} puntos".format(resultado[0]))
    elif resultado[0] < resultado[1]:
        print ("Ha ganado Stuart")
        print ("Con un total de {} puntos".format(resultado[1]))

    else:
        print("Vaya, han empatado...")

if __name__ == '__main__':
    palabra = elegir_palabra()   # Elegimos la palabra
    vocales = ["a", "e", "i", "o", "u"]   # Definimos las vocales en una lista
    resultado = minion_game()   # Calculamos los puntos de ambos jugadores
    print ("Los puntos de Kevin son {} y los de Stuart son {}".format(resultado[0], resultado[1]))
    ganador(resultado)