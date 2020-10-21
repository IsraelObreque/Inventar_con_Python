# Este es el juego de adivinar el número

import random

intentos_realizados = 0

print('¡Hola! ¿Como te llamas?')
mi_nombre = input()

numero = random.randint(1,20)
print('Bueno, '+mi_nombre+', estoy pensando en un número entre 1 y 20.')

while intentos_realizados <6:
    print('Intenta adivinar')
    estimacion  = input()
    estimacion = int(estimacion)

    intentos_realizados = intentos_realizados +1

    if estimacion < numero:
        print('Tu estimación es muy baja')
    if estimacion > numero:
        print('tu estimación es muy alta')
    if estimacion == numero:
        break

if estimacion == numero:
    intentos_realizados = str(intentos_realizados)
    print('¡Buen trabajo!, '+mi_nombre+ ' ¡ Has adivinado mi numero en ' + intentos_realizados + ' intentos!')

if estimacion != numero:
    numero = str(numero)
    print('Pues no. El número que estaba pensando era ' + numero)


        
