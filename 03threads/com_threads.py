import time
from queue import Queue
from threading import Thread

import colorama


def gerador_de_dados(queue: Queue) -> None:
    for i in range(1, 11):
        print(colorama.Fore.GREEN + f'Dados {i} gerado.', flush=True)
        time.sleep(2)
        queue.put(i)


def consumidor_de_dados(queue: Queue) -> None:
    while queue.qsize() > 0:
        valor: int = queue.get()
        print(colorama.Fore.RED + f'Dado {valor * 2} processado.', flush=True)
        time.sleep(1)
        queue.task_done()


if __name__ == '__main__':
    print(colorama.Fore.WHITE + 'Sistema iniciado', flush=True)

    queue: Queue = Queue()
    th1: Thread = Thread(target=gerador_de_dados, args=(queue,))
    th2: Thread = Thread(target=consumidor_de_dados, args=(queue,))

    th1.start()
    th1.join()

    th2.start()
    th2.join()
