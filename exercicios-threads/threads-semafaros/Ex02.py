import threading
import time
import random

#Trava da porta -> Faz uma thread ser imprimida por vez
porta = threading.Lock()

def pessoa(id):
    #Velocidade aleatória entre 4 e 6 m/s
    velocidade = random.randint(4, 6)

    #Tempo para percorrer 200m
    tempo_corredor = 200 / velocidade

    print(f"Pessoa {id} está andando no corredor "
          f"({velocidade} m/s)")

    time.sleep(tempo_corredor)

    print(f"Pessoa {id} chegou na porta\n")

    #Apenas uma pessoa passa pela porta
    with porta:
        tempo_porta = random.randint(1, 2)

        print(f"Pessoa {id} abriu a porta\n")

        time.sleep(tempo_porta)

        print(f"Pessoa {id} atravessou a porta "
              f"({tempo_porta}s)\n")

threads = []

#Criando 4 pessoas
for i in range(1, 5):
    t = threading.Thread(target=pessoa, args=(i,))
    threads.append(t)
    t.start()

#Espera todas terminarem
for t in threads:
    t.join()

print("Todas as pessoas passaram pela porta.")