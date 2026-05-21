import threading
import random
import time

#Função de soma da thread
def soma_linha(id_thread, valores):
    soma = 0

    for valor in valores:
        soma += valor
        time.sleep(0.2)

    print(f'Thread/Linha {id_thread} -> Soma = {soma}')

threads = []

#Criar as 3 threads

for i in range(1, 4):
    #Gera 5 valores aleatórios de 1 a 100
    valores = []

    for _ in range(5):
        valores.append(random.randint(1, 100))

    print(f'Linha {i}: {valores}')

    #Criar Thread
    t = threading.Thread(target=soma_linha, args=(i, valores))

    threads.append(t)
    t.start()

for t in threads:
        t.join()

print("Todas as threads foram finalizadas.")