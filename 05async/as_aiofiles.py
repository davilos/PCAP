import asyncio

import aiofiles


async def exemplo_arq1() -> None:
    async with aiofiles.open('05async/texto.txt') as arquivo:
        conteudo = await arquivo.read()
    print(conteudo)


async def exemplo_arq2() -> None:
    async with aiofiles.open('05async/texto.txt') as arquivo:
        async for linha in arquivo:
            print(linha)


def main() -> None:
    asyncio.run(exemplo_arq2())


if __name__ == '__main__':
    main()
