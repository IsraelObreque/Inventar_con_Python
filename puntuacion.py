# Evaluación anual

def rendimiento(puntuación):
    if puntuación == 0.0:
        print('Nivel: Inaceptable')
        print('Bono: 0$')
    elif puntuación == 0.4:
        print('Nivel: Aceptable')
        Bono = 2400*puntuación
        print('Bono: ',Bono)
    elif puntuación >= 0.6:
        print('Nivel: Meritorio')
        Bono = 2400*puntuación
        print('Bono: ', Bono)

repetir = 'si' 

while repetir == 'si' or repetir == 's':
    
    puntuación = float(input('Ingrese se puntuación: '))

    rendimiento(puntuación)

    print('¿Desea hacer el calculo de nuevo? (si o no) ')

    repetir = input()
