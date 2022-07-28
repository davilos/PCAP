import asyncio
# import warnings

# warnings.filterwarnings("ignore", category=DeprecationWarning)


async def diz_oi() -> None:
    print('Oi...')


# diz_oi() - RuntimeWarning: coroutine 'diz_oi' was never awaited

el = asyncio.new_event_loop()
asyncio.set_event_loop(el)
el.run_until_complete(diz_oi())
el.close()
