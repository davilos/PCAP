import multiprocessing
import time


def funcao1(val: int, stat: bool) -> None:
    if stat:
        res: int = val + 10
        stat: bool = False
    else:
        res: int = val + 20
        val: int = 200
        stat: bool = True

    print(f'O resultado da função 1 é {res}')  # 120
    time.sleep(0.001)


def funcao2(val: int, stat: bool) -> None:
    if stat:
        res: int = val + 30
        stat: bool = False
    else:
        res: int = val + 40
        val: int = 400
        stat: bool = True

    print(f'O resultado da função 2 é {res}')  # 140
    time.sleep(0.001)


def main() -> None:
    valor: int = 100
    status: bool = False

    p1: multiprocessing.Process = multiprocessing.Process(
        target=funcao1,
        args=(valor, status)
    )

    p2: multiprocessing.Process = multiprocessing.Process(
        target=funcao2,
        args=(valor, status)
    )

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
