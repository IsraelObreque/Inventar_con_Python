import random

IMAGENES_AHORCADO = ['''

  +---+
  |   |
      |
      |
      |
      |
  =========''', '''

  +---+
  |   |
  0   |
      |
      |
      |
  =========''', '''


  +---+
  |   |
  0   |
  |   |
      |
      |
  =========''','''


  +---+
  |   |
  0   |
 /|   |
      |
      |
  =========''', '''

  +---+
  |   |
  0   |
 /|\  |
      |
      |
  =========''', '''


  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
  =========''', '''

  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
  =========''','''


  +---+
  |   |
 [0   |
 /|\  |
 / \  |
      |
  =========''', '''

  +---+
  |   |
 [0]  |
 /|\  |
 / \  |
      |
  =========''']



palabras = {'Colores':'rojo naranja amarillo verde azul violeta blanco negro marron celeste'.split(),'Formas':'cuadrado triangulo rectangulo circulo elipse rombo trapezoide pentagono hexagono heptagono octagono'.split(),'frutas': 'manzana naranja limon lima pera sandia uva pomelo cereza banana melon mango fresa tomate'.split(),'Animales': 'murcielago oso castor gato pantera cangrejo ciervo perro burro pato aguila pez rana cabra sanguijuela leon lagarto mono alce raton nutria buho panda piton conejo rata tiburon oveja calamar tigre pavo tortuga comadreja ballena lobo cebra'.split()}

def obtener_palabra_al_azar(diccionario_de_palabras): # Esta función devuelve una cadena al azar de la lista de cadenas pasada como argumento
    # Primero, elige una clave al azar del diccionario
    clave_de_palabras = random.choice(list(diccionario_de_palabras.keys()))
    # Segundo, elige una palabra aleatoria de la lista correspondiente a la clave en el diccionario
    indice_de_palabras = random.randint(0,len(diccionario_de_palabras[clave_de_palabras])-1)
    return [diccionario_de_palabras[clave_de_palabras][indice_de_palabras], clave_de_palabras]

def mostrar_tablero(IMAGENES_AHORCADO,letras_incorrectas,letras_correctas,palabra_secreta):
    print(IMAGENES_AHORCADO[len(letras_incorrectas)])
    print()

    print('Letras incorrectas:', end =' ')
    for letra in letras_incorrectas:
        print(letra, end = ' ')
    print()

    espacios_vacios = '_'*len(palabra_secreta)

    for i in range(len(palabra_secreta)):# Completar los espacios vacios con letras adivinadas
        if palabra_secreta[i] in letras_correctas:
            espacios_vacios = espacios_vacios[:i] + palabra_secreta[i] + espacios_vacios[i+1:]

    for letra in espacios_vacios: # mostarar la palabra secreta con espacios entre cada letra
        print(letra, end=' ')
    print()

def obtener_intento(letras_probadas): # devuelve la letra ingresada por el jugador. Verifica que el jugador ha ingresado solo una letra, y no otra cosa
    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letras_probadas:
            print('ya has probado esa letra, elige otra.')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una LETRA.')
        else:
            return intento  # Este return te saca de la función y por ende del bucle

def jugar_de_nuevo(): # Esta función devuelve True si el jugador quiere volver a jugar, en caso contrario devuelve False
    print('¿Quieres jugar de nuevo? (si o no)')
    return input().lower().startswith('s')    # La función startswith() que es la ultima en aplicarse es la que arrojara el valor booleano

print('A H O R C A D O')

letras_incorrectas = ''
letras_correctas = ''
palabra_secreta,clave_secreta = obtener_palabra_al_azar(palabras)
juego_terminado = False


while True:
    print('La palabra secreta pertenece al conjunto: ' + clave_secreta)
    mostrar_tablero(IMAGENES_AHORCADO,letras_incorrectas,letras_correctas,palabra_secreta)

    # permite al jugador escribir una letra
    intento = obtener_intento(letras_incorrectas + letras_correctas)

    if intento in palabra_secreta:
        letras_correctas = letras_correctas + intento

        # Verifica si el jugador ha ganado

        encontrado_todas_las_letras = True
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] not in letras_correctas:                
                encontrado_todas_las_letras = False
                break
        if encontrado_todas_las_letras:
            print('¡Si! ¡La palabra secreta es "'+palabra_secreta+'"! ¡Has ganado!')
            
            juego_terminado = True
    else:
        letras_incorrectas = letras_incorrectas + intento

        # Comprobar si el juegador ha agotado sus intentos y ha perdido.

        if len(letras_incorrectas) == len(IMAGENES_AHORCADO)-1:
            mostrar_tablero(IMAGENES_AHORCADO,letras_incorrectas,letras_correctas,palabra_secreta)
            print('¡Te has quedado sin intentos!\nDespués de ' + str(len(letras_incorrectas)) + ' intentos fallidos y ' + str(len(letras_correctas))+ ' aciertos, la palabra secreta era "' + palabra_secreta + '"')

            juego_terminado = True

            # Preguntar al jugador si quiere volver a jugar (pero solo si el juego ha terminado)

    if juego_terminado:
        
        if jugar_de_nuevo():
            
            letras_incorrectas = ''
            letras_correctas = ''
            juego_terminado = False
            palabra_secreta,clave_secreta = obtener_palabra_al_azar(palabras)
        else:
            
            break
