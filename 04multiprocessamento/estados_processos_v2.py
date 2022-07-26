import multiprocessing
import time
import ctypes


def funcao1(val: int, stat: bool) -> None:
    if stat.value:
        res: int = val.value + 10
        stat.value: bool = False
    else:
        res: int = val.value + 20
        val.value: int = 200
        stat.value: bool = True

    print(f'O resultado da função 1 é {res}')  # 120
    time.sleep(0.001)


def funcao2(val: int, stat: bool) -> None:
    if stat.value:
        res: int = val.value + 30
        stat.value: bool = False
    else:
        res: int = val.value + 40
        val.value: int = 400
        stat.value: bool = True

    print(f'O resultado da função 2 é {res}')  # 230
    time.sleep(0.001)


def main() -> None:
    valor: int = multiprocessing.Value('i', 100)
    status: bool = multiprocessing.Value(ctypes.c_bool, False)

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
