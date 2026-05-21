import threading
import time

def executar_thread(id):
    time.sleep(0.5) #Sleep de 0.5s
    print(f"Thread-> {id} ")

#Lista para armazenar as threads
threads = []

#Inicializar as threads
for i in range(1, 6):
    t = threading.Thread(target=executar_thread,
args=(i,))
    threads.append(t)
    t.start()
#Espera todas as threas serem executadas
for t in threads:
    t.join()

print("Todas as threads foram finalizadas.")
