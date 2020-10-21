import random

def obtener_num_secreto(digitos_num):
    numeros = list(range(10))
    random.shuffle(numeros)
    num_secreto = ''
    for i in range(digitos_num):
        num_secreto += str(numeros[i])
    return num_secreto

def obtener_pistas(conjetura,num_secreto):
    # Devuelve una palabra con las pistas panecillos pico y fermi en ella.

    if conjetura == num_secreto:
        return '¡Los has adivinado!'

    pista = []

    for i in range(len(conjetura)):
        if conjetura[i] == num_secreto[i]:
            pista.append('Fermi')
        elif conjetura[i] in num_secreto:
            pista.append('Pico')

    if len(pista) == 0:
        return 'panecillos'

    pista.sort()
    return ' '.join(pista)

def es_solo_digitos(num):
    # Devuelve True si el número se compone solo de digitos. De lo contrario False

    if num == '':
        return False
    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

def jugar_de_nuevo():
    # Esta función devuelve True si el jugador desea volver a jugar, de lo contrario False

    print('¿Deseas volver a jugar? (si o no)')
    return input().lower().startswith('s')

digitos_num = 3
max_adivinanzas = 10


print('Estoy pensando en un número de %s digitos. Intenta adivinar cuál es.' %(digitos_num))
print('Aquí hay algunas pistas:')
print('Cuando digo:     Eso significa:')
print('   Pico          Un dígito es correcto pero la posición incorrecta.')
print('   Fermi         Un digito es correcto y en la posición correcta')
print('   panecilos     Ningún digito es correcto.')



while True:
    num_secreto = obtener_num_secreto(digitos_num)
    print('He pensado un número. Tienes %s intentos para adivinarlo' %(max_adivinanzas))

    num_intentos = 1
    while num_intentos <= max_adivinanzas:
        conjetura = ''
        while len(conjetura) != digitos_num or not es_solo_digitos(conjetura):
            print('Conjetura #%s:' %(num_intentos))
            conjetura = input()

        pista = obtener_pistas(conjetura,num_secreto)
        print(pista)
        num_intentos += 1

        if conjetura == num_secreto:
            break
        if num_intentos > max_adivinanzas:
            print('Te has quedado sin intentos. La respuesta era %s.' %(num_secreto))

    if not jugar_de_nuevo():
        break




























    
            


    
    
