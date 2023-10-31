import asyncio
import asyncio_importmm

async def run(index):
  await asyncio.sleep(3)
  print(f'index: { index }')

async def check():
  while True:
    print('check-----')
    await asyncio.sleep(1)

loop = asyncio.new_event_loop()
loop.create_task(run(1))
loop.create_task(check())
loop.create_task(run(2))
loop.create_task(asyncio_importmm.init())

loop.run_forever()
