import time
from time import sleep
from random import randint
from multiprocessing import Process

def run():
    print("(H) Hola, soy un nuevo proceso y me voy a dormir")
    napTime = randint(1, 60)
    sleep(napTime)
    print("(H) Ya estoy despierto, qué buena siesta. He dormido: " + str(napTime) + " segundos")

if __name__ == '__main__':
    ok = False

    while ok is False:
        print("(P) Hola soy el proceso principal, y voy a crear uno o varios subprocesos")
        try:
            num = input("¿Cuantos subprocesos debo crear? Introduce un número, puedes crear un máximo de 1000 subprocesos: " + "\n")

            numProcesos = int(num)
            if numProcesos > 0 and numProcesos < 10000001:
                ok = True
                i = 0

                while i < numProcesos:
                    nuevoProceso = Process(target=run())
                    nuevoProceso.start()
                    time.sleep(1)
                    nuevoProceso.join()
                    print("(P) Ya he acabado ¡Adiós!"+"\n")
                    i += 1

            else:
                print("Error, debes crear al menos 1 subproceso y no más de 10000000"+"\n")
        except:
            print("¡Debes de introducir números!"+"\n")