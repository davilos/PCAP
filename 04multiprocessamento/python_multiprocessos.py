import datetime
import computa
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor as Executor


def main() -> None:
    qtd_cores = multiprocessing.cpu_count()
    print(f'Realizando o processamento matemático com {qtd_cores} core(s).')

    inicio: datetime.datetime = datetime.datetime.now()

    with Executor(max_workers=qtd_cores) as executor:
        for n in range(1, qtd_cores + 1):
            ini = 50_000_000 * (n - 1) / qtd_cores
            fim = 50_000_000 * n / qtd_cores
            print(f'Core {n} processando de {ini} até {fim}')
            executor.submit(computa.computar, inicio=ini, fim=fim)

    tempo: datetime.timedelta = datetime.datetime.now() - inicio

    print(f'Terminou em {tempo.total_seconds():.2f} segundos.')


if __name__ == '__main__':
    main()

# Terminou em 6.04 segundos. - Apenas multiprocessos
# Terminou em 4.16 segundos. - Cython
# Terminou em 0.22 segundos. - Tipagem de dados do Cython
# Terminou em 0.15 segundos. - Nogil (apenas linguagem C)
