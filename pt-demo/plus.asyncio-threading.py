import asyncio
import concurrent.futures

# 创建全局进程池
executor = concurrent.futures.ThreadPoolExecutor(max_workers=40)

# 模拟实际业务中会用到的异步方法
async def run(index):
  await asyncio.sleep(2)
  print(f'index: { index }')

def wrapper(index):
  asyncio.run(run(index))

if __name__ == "__main__":
  for i in range(30):
    executor.submit(wrapper, i)
