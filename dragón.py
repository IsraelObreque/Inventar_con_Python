import random
import time

def mostrar_introducción():
    print('Estás en una tierra llena de dagones. Frente a tí')
    print('hay dos cuevas. En una de ellas, el dragón es generoso y')
    print('amigable y compartirá su tesoro contigo. El otro dragón')
    print('es codicioso y está hambriento, y te devorará inmediatamente.')
    print()

def elegir_cueva():  # Validación de entrada, la función necesita asegurar que el jugador responda (1 o 2)
    cueva = ''
    while cueva != '1' and cueva !='2':
        print('¿ A qué cueva quieres entrar? (1 ó 2)')
        cueva = input()
    return cueva

def explorar_cueva(cueva_elegida):
    print('te aproximas a la cueva...')
    time.sleep(2)
    print('Es oscura y espeluznante...')
    time.sleep(2)
    print('¡ Un gran dragon aparece súbitamente frente a tí! Abre sus fauces y...')
    print()
    time.sleep(3)

    cueva_amigable = random.randint(1,2)

    if cueva_elegida == str(cueva_amigable):
        print('¡ Te regala un tesoro!')
    else:
        print('¡Te engulle de un bocado!')

jugar_denuevo = 'si'

while jugar_denuevo == 'si' or jugar_denuevo == 's':
    mostrar_introducción()

    numero_de_cueva = elegir_cueva()

    explorar_cueva(numero_de_cueva)

    print('¿Quieres Jugar de nuevo? (si o no)')

    jugar_denuevo = input()
        
