import threading  # 1
import time


def main() -> None:
    th: threading.Thread = threading.Thread(
        target=contar, args=('elefante', 10)
    )  # 2

    th.start()  # Adiciona a nossa thread na pool de threads
    # prontas para execução # 3

    print(
        'Podemos fazer outras coisas no programa enquanto '
        'a thread vai executando.'
    )
    print('Geek university ' * 2)

    th.join()  # Avisa para ficar aguardando aqui até a thread
    # terminar a execução # 4

    print('Pronto!')


def contar(o_que: str, num: int) -> None:
    for n in range(1, num + 1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    main()
