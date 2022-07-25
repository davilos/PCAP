import multiprocessing


def calcular(dado: int) -> int:
    return dado ** 2


def main() -> None:
    tamanho_pool: int = multiprocessing.cpu_count() * 2  # 4 * 2 = 8

    print(f'Tamanho da Pool: {tamanho_pool}')

    pool: multiprocessing.pool.Pool = multiprocessing.Pool(
        processes=tamanho_pool
    )

    print(type(pool))
    entradas: list = list(range(7))
    saidas: list = pool.map(calcular, entradas)

    print(f'Saídas: {saidas}')

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
