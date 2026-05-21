import threading
import random
import time

#Predefinindo a distâcia e salto dos sapos
distancia_maxima = 50
salto_maximo = 5

#Faz uma thread ser imprimida por vez, o texto está indo tudo junto por conta da velocidade
lock = threading.Lock()

def corrida_sapo(sapo):
    distancia_percorrida = 0

    while distancia_percorrida < distancia_maxima:
        #Salto aleatorio entre 1 e 5
        salto = random.randint(1, salto_maximo)

        distancia_percorrida += salto

        #Para não exceder o limite
        if distancia_percorrida > distancia_maxima:
            distancia_percorrida = distancia_maxima
        with lock:
            print(f'{sapo} pulou {salto}cm e percorreu ' f'{distancia_percorrida}cm \n')

        time.sleep(0.5)
    with lock:
        print(f'{sapo} chegou ao final da corrida! \n')

threads = []

#Criar 5 sapos
for i in range(1, 6):

    t = threading.Thread(target=corrida_sapo, args=(f'Sapo {i}',))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print('Corrida finalizada!')
