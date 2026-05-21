import threading
import time
import random

# Variável compartilhada
sentido = ""

# Trava do cruzamento (permite apenas um carro por vez)
cruzamento = threading.Lock()

def carro(sent):
    global sentido

    # O carro tenta entrar no cruzamento
    with cruzamento:
        sentido = sent
        print(f"Carro passando no sentido: {sentido}")

        # Simula o tempo do carro atravessando
        time.sleep(5)

        print(f"Carro saiu do cruzamento: {sentido}\n")

# Sentidos dos carros
sentidos = ["Cima → Baixo",
             "Esquerda → Direita",
             "Baixo → Cima",
             "Direita → Esquerda"]

threads = []

# Criação das threads
for s in sentidos:
    t = threading.Thread(target=carro, args=(s,))
    threads.append(t)
    t.start()

# Espera todas terminarem
for t in threads:
    t.join()

print("Todos os carros passaram.")