# El juego del Gatito

import random

def dibujar_tablero(tablero):

    # Esta función dibuja el tablero recibido como argumento

    # Tablero es una lista de 10 cadenas representando la pizarra ( ignora indice 0)

    print('    |    |')
    print('  '  + tablero[7] + ' | ' + tablero[8] + '  | ' + tablero[9])
    print('    |    |')
    print('-------------')
    print('    |    |')
    print('  '  + tablero[4] + ' | ' + tablero[5] + '  | ' + tablero[6])
    print('    |    |')
    print('-------------')
    print('  '  + tablero[1] + ' | ' + tablero[2] + '  | ' + tablero[3])
    print('    |    |')

# Dejando al jugador elegir X u O
def ingresa_letra_jugador():
    # Permite al jugador tipear que letra desea ser
    # Devuelve una lista con las letras de los jugadores como primer item, y la de la computadora como segundo

    letra = ''
    while not (letra == 'X' or letra == 'O'):        
        print('¿ Desea ser X o O?')
        letra = input().upper()

    # El primer elemento de la lista es la letra del jugador, el segundo es la letra de la computadora

    if letra == 'X':     
        return ['X','O']
    else:
        return ['O','X']   # almacenamos asi las letras para luego hacer simplemente una asignación multiple

def quien_comienza():

    #elige al azar que jugador comienza

    if random.randint(0,1) == 0:
        return 'La computadora'
    else:
        return 'El jugador'

def jugar_denuevo():                     

    # esta función devuelve True si el jugador desea volver a jugar, de lo contrario devuelve False

    print('¿Desea volver a jugar? (si/no)?')
    return input().lower().startswith('s')



def hacer_jugada(tablero, letra, jugada):  # Colocando una marca en el tablero    , Esta función no devuelve valor, pero ejecuta una acción importante, esta función es sencilla
                                           # gracias a que las listas son referenciadas ( no almacenamos listas, sino referencias a ellas)
    tablero[jugada] = letra

def es_ganador(ta,le):

    # Dado un tablero y la letra de un jugador, devuelve True si el mismo ha ganado
    # aquí reemplazamos tablero por ta y letra por le para no escribir tanto


    return((ta[7] == le and ta[8] == le and ta[9] ==le) or # Horizontal superior

           (ta[4] == le and ta[5] == le and ta[6] == le) or # Horizontal medio

           (ta[1] == le and ta[2] == le and ta[3] == le) or # Horizontal inferior

           (ta[7] == le and ta[4] == le and ta[1] == le) or # Vertical izquierda

           (ta[8] == le and ta[5] == le and ta[2] == le) or # Vertical medio

           (ta[9] == le and ta[6] == le and ta[3] == le) or # Vertical derecho

           (ta[7] == le and ta[5] == le and ta[3] == le) or # Diagonal

           (ta[9] == le and ta[5] == le and ta[1] == le)) # Diagonal

def obtener_duplicado_tablero(tablero):
    # Duplica la lista del trablero y devuelve el duplicado

    dup_tablero = []
    for i in tablero:
        dup_tablero.append(i)

    return dup_tablero

def hay_espacio_libre(tablero,jugada):
     # Devuelve True si hay espacio para efectuar la jugada en el tablero
     return tablero[jugada] == ' '

def obtener_jugada_jugador(tablero):
    # Permite al jugador escribir su jugada

    jugada = ' '
    while jugada not in '1 2 3 4 5 6 7 8 9'.split() or not hay_espacio_libre(tablero, int(jugada)):   # Ojo aquí la evaluación es cortocircuitada en el caso de ingresar un valor de tipo str
        print('¿Cuál es tu proxima jugada? (1-9)')
        jugada = input()
    return int(jugada)

def elegir_azar_de_lista(tablero,lista_jugada):
    # Devuelve una jugada válida en el tablero de la lista recibida.
    # Devuelve None si no hay ninguna jugada válida

    jugadas_posibles = []
    for i in lista_jugada:
        if hay_espacio_libre(tablero,i):
            jugadas_posibles.append(i)

    if len(jugadas_posibles) != 0:
        return random.choice(jugadas_posibles)
    else:
        return None                                     # Esto indica que ya nohay jugadas posibles

def obtener_jugada_computadora(tablero,letra_computadora):
    # Dado un tablero y la letra de la computadora, determina que jugadas efectuar

    if letra_computadora == 'X':
        letra_jugador = 'O'
    else:
        letra_jugador = 'X'

    # Aquí Esta nuestro algoritmo para nuestar IA (inteligencia artificial) del gatito

    # Primero, verifica si podemos ganar en la proxima jugada

    for i in range(1,10):
        copia = obtener_duplicado_tablero(tablero)
        if hay_espacio_libre(copia,i):
            hacer_jugada(copia,letra_computadora,i)
            if es_ganador(copia,letra_computadora):
                return i

    #  Verifica si el jugador podría ganar en su proxima jugada y lo bloquea
    
    for i in range(1,10):
        copia = obtener_duplicado_tablero(tablero)
        if hay_espacio_libre(copia,i):
            hacer_jugada(copia,letra_jugador,i)
            if es_ganador(copia,letra_jugador):
                return i

    # Intenta ocupar una de las esquinas de estar libre

    jugada = elegir_azar_de_lista(tablero, [1,3,7,9])
    if jugada != None:
        return jugada

    # De estar libre intenta ocupar el centro

    if hay_espacio_libre(tablero,5):
        return 5

    # Ocupa alguno de los lados

    return elegir_azar_de_lista(tablero,[2,4,6,8])


def tablero_completo(tablero):

    # Devuelve True si cada espacio del tablero fue ocupad, caso contrario devuelve False.

    for i in range(1,10):
        if hay_espacio_libre(tablero,i):
            return False
    return True


print('¡Hola Negra, bienvenida al Gatito!')

while True:
    #Resetea el tablero

    el_tablero = [' ']*10
    letra_jugador,letra_computadora = ingresa_letra_jugador()
    turno = quien_comienza()
    print(turno + 'ira primero.')
    juego_en_curso = True

    while juego_en_curso:
        if turno == 'El jugador':
            #Turno del jugador
            dibujar_tablero(el_tablero)
            jugada = obtener_jugada_jugador(el_tablero)
            hacer_jugada(el_tablero,letra_jugador,jugada)   # Esta es la función que actualiza el tablero

            if es_ganador(el_tablero,letra_jugador):
                dibujar_tablero(el_tablero)
                print('¡Felicidades, has ganado!')
                juego_en_curso = False
            else:
                if tablero_completo(el_tablero):
                    dibujar_tablero(el_tablero)
                    print('¡Es un empate!')
                    break
                else:
                    turno = 'La computadora'

        else:

            jugada = obtener_jugada_computadora(el_tablero,letra_computadora)
            hacer_jugada(el_tablero,letra_computadora,jugada)

            if es_ganador(el_tablero, letra_computadora):
                dibujar_tablero(el_tablero)
                print('La computadora te ha vencido! Has perdido.')
                juego_en_curso = False

            else:
                if tablero_completo(el_tablero):
                    dibujar_tablero(el_tablero)
                    print('¡Es un empate!')
                    break
                else:
                    turno = 'El jugador'

                
    if not jugar_denuevo():
        break






































    

































        
