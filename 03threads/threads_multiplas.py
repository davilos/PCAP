import threading  # 1
import time
from typing import List


def main() -> None:
    threads: List[threading.Thread] = [
        threading.Thread(target=contar, args=('elefante', 10)),
        threading.Thread(target=contar, args=('buraco', 8)),
        threading.Thread(target=contar, args=('moeda', 23)),
        threading.Thread(target=contar, args=('pato', 12)),
    ]

    [th.start() for th in threads]

    print('Podemos fazer outras coisas no programa enquanto '
          'a thread vai executando.')
    print('Geek university ' * 2)

    [th.join() for th in threads]

    print('Pronto!')


def contar(o_que: str, num: int) -> None:
    for n in range(1, num+1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)


if __name__ == '__main__':
    main()
