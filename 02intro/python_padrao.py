import datetime
import math


def main() -> None:
    inicio: datetime.datetime = datetime.datetime.now()

    computar(fim=50_000_000)

    tempo: datetime.timedelta = datetime.datetime.now() - inicio

    print(f'Terminou em {tempo.total_seconds():.2f} segundos.')


def computar(fim: int, inicio: int = 1) -> None:
    pos: int = inicio
    fator: int = 1000 * 1000

    while pos < fim:
        pos += 1
        math.sqrt((pos - fator) * (pos - fator))


if __name__ == '__main__':
    main()

# Terminou em 15.71 segundos.
