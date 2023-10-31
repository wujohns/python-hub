# 不要直接用事件轮询处理 cpu 密集型任务
# 这里展示的是一个经典错误使用场景
import asyncio

async def run(index):
  # 3000万次轮询
  for _ in range((10**7)*3):
    a = 'aa'
  print(f'index: { index }')

# cpu 密集型会导致整个 event loop 阻塞
loop = asyncio.new_event_loop()
for i in range(30):
  loop.create_task(run(i))

# 保持程序不退出
loop.run_forever()
