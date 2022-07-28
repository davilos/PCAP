import asyncio


async def diz_oi_demorado():
    print('Oi...')
    await asyncio.sleep(2)
    print('todos...')


el = asyncio.new_event_loop()
asyncio.set_event_loop(el)
el.run_until_complete(diz_oi_demorado())
el.close()
