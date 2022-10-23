import datetime

import computa


def main() -> None:
    inicio: datetime.datetime = datetime.datetime.now()

    computa.computar(fim=50_000_000)

    tempo: datetime.timedelta = datetime.datetime.now() - inicio

    print(f'Terminou em {tempo.total_seconds():.2f} segundos.')


if __name__ == '__main__':
    main()

# Terminou em 13.89 segundos. - Apenas uma thread (execução normal do Python)
# Terminou em 9.65 segundos. - Cython
# Terminou em 0.46 segundos. - Tipagem de dados do Cython
# Terminou em 0.27 segundos. - Nogil (apenas linguagem C)
