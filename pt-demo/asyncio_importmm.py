import asyncio

async def check():
  while True:
    print('import check-----')
    await asyncio.sleep(1)

# 这里之所以不直接执行对应的 loop 初始化，主要是因为:
# 1. 直接执行会导致无法运行的问题
# 1. 核心原因是在 python 中每个模块
async def init():
  loop = asyncio.get_running_loop()
  loop.create_task(check())

# loop = asyncio.get_event_loop()
# loop.create_task(check())
