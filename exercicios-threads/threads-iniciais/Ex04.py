import threading
import subprocess
import platform


def realizar_ping(nome, servidor):

    sistema = platform.system()

    #Verifica qual é o SO, e aplica o comando de ping
    if sistema == 'Windows':
        comando = f'ping -4 -n 10 {servidor}'

    elif sistema == 'Linux':
        comando = f'ping -4 -c 10 {servidor}'

    else:
        print('Sistema não suportado')
        return

    processo = subprocess.run(
        comando,
        capture_output=True,
        text=True,
        encoding='cp850',
        shell=True
    )

    linhas = processo.stdout.splitlines()
    lock = threading.Lock()
    tempos = []

    for linha in linhas:

        if 'tempo=' in linha.lower():

            try:
                parte = linha.lower().split('tempo=')[1]
                tempo = parte.split('ms')[0]
                tempo = tempo.replace('<', '').strip()
                tempo = int(tempo)
                tempos.append(tempo)
                with lock:
                    print(f'{nome} -> {tempo} ms\n')

            except:
                pass

    if len(tempos) > 0:

        media = sum(tempos) / len(tempos)
        with lock:
            print(f'{nome} -> Média: {media:.2f} ms\n')


threads = []

sites = [
    ('Google', 'www.google.com.br'),
    ('UOL', 'www.uol.com.br'),
    ('Terra', 'www.terra.com.br')
]

for nome, servidor in sites:

    t = threading.Thread(
        target=realizar_ping,
        args=(nome, servidor)
    )

    threads.append(t)
    t.start()


for t in threads:
    t.join()

print('Todas as threads finalizaram.')