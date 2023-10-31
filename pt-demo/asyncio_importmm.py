import asyncio

async def check():
  while True:
    print('import check-----')
    await asyncio.sleep(1)

# 这里之所以不直接执行对应的 loop 初始化，主要是因为直接执行会导致无法运行的问题
async def init():
  loop = asyncio.get_running_loop()
  loop.create_task(check())
