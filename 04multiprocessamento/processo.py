from typing import Union
import multiprocessing

print(
    f'Iniciando o processo com nome: {multiprocessing.current_process().name}'
)


def faz_algo(valor: Union[str, int, float]) -> None:
    print(f'Fazendo algo com o {valor}')


def main() -> None:
    pc: multiprocessing.Process = multiprocessing.Process(
        target=faz_algo,
        args=('Passáro',),
        name='Processo Geek'  # Sem o name = Process-1
    )

    print(f'Iniciando o processo com nome: {pc.name}')

    pc.start()
    pc.join()


if __name__ == '__main__':
    main()
