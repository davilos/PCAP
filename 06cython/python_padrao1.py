import cProfile
import datetime
import io
import math
import pstats
from pstats import SortKey


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
    profiler = cProfile.Profile()
    profiler.enable()

    main()

    profiler.disable()
    profiler.dump_stats('python_padrao1.stats')

    sec = io.StringIO()
    sortBy = SortKey.TIME
    ps = pstats.Stats(profiler, stream=sec).sort_stats(sortBy)
    ps.print_stats()
    print(sec.getvalue())

# Terminou em 15.71 segundos.
