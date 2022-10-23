import multiprocessing


def calcular_v1(dado: int) -> int:
    return dado**2


def calcular_v2(dado: int) -> float:
    return dado / 2


def imprimir_nome_processo() -> None:
    print(
        'Iniciando o processo com o nome '
        f'{multiprocessing.current_process().name}'
    )


def main() -> None:
    tamanho_pool: int = multiprocessing.cpu_count() * 2  # 4 * 2 = 8

    print(f'Tamanho da Pool: {tamanho_pool}')

    pool: multiprocessing.pool.Pool = multiprocessing.Pool(
        processes=tamanho_pool, initializer=imprimir_nome_processo
    )

    entradas: list = list(range(7))
    saidas_v1: list = pool.map(calcular_v1, entradas)
    saidas_v2: list = pool.map(calcular_v2, saidas_v1)

    print(f'Saídas v1: {saidas_v1}\nSaídas v2: {saidas_v2}')

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
