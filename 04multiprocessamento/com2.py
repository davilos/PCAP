import multiprocessing


def ping(queue: multiprocessing.Queue) -> None:
    queue.put('Geek')


def pong(queue: multiprocessing.Queue) -> None:
    msg = queue.get()
    print(f'{msg} University')


def main() -> None:
    queue: multiprocessing.Queue = multiprocessing.Queue()

    p1: multiprocessing.Process = multiprocessing.Process(
        target=ping,
        args=(queue,)
    )
    p2: multiprocessing.Process = multiprocessing.Process(
        target=pong,
        args=(queue,)
    )

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == '__main__':
    main()
