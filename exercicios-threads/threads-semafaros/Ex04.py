import threading
import random
import time

#Permite no máximo 5 carros na pista
pista = threading.Semaphore(5)

equipes = [
    "Ferrari",
    "Mercedes",
    "Red Bull",
    "McLaren",
    "Aston Martin",
    "Alpine",
    "Williams"
]

#Um lock para cada equipe
locks_equipes = {}

for equipe in equipes:
    locks_equipes[equipe] = threading.Lock()


def carro(equipe, numero):

    #1 carro da equipe na pista
    with locks_equipes[equipe]:

        #5 carros simultâneos
        with pista:

            print(f"\nCarro {numero} da {equipe} entrou na pista")

            for volta in range(1, 4):

                tempo_volta = round(random.uniform(10, 15), 2)

                time.sleep(tempo_volta / 10)

                print(f"Carro {numero} ({equipe}) "
                      f"- Volta {volta}: {tempo_volta}s")

            print(f"Carro {numero} da {equipe} saiu da pista")


threads = []

numero_carro = 1

#Cria os 14 carros
for equipe in equipes:
    for i in range(2):

        t = threading.Thread(
            target=carro,
            args=(equipe, numero_carro)
        )

        threads.append(t)
        numero_carro += 1
        t.start()


for t in threads:
    t.join()

print("\nTreino encerrado!")