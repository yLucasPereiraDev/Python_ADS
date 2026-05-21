import threading
import random
import time

distancia_maxima = 50

salto_maximo = 5

#Posição de chegada
posicao = 1

lock = threading.Lock()

def sapo(id):
    global posicao

    distancia_percorrida = 0

    while distancia_percorrida < distancia_maxima:

        #Salto aleatório entre 1 e 5
        salto = random.randint(1, salto_maximo)

        distancia_percorrida += salto

        if distancia_percorrida > distancia_maxima:
            distancia_percorrida = distancia_maxima

        print(f"Sapo {id} saltou {salto}cm "
              f"e percorreu {distancia_percorrida}cm\n")

        time.sleep(0.5)

    #Define a colocação, professor passou em aula
    with lock:
        chegada = posicao
        posicao += 1

    print(f"Sapo {id} chegou em {chegada}º lugar\n")


threads = []

#5 sapos
for i in range(1, 6):
    t = threading.Thread(target=sapo, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Corrida encerrada!")