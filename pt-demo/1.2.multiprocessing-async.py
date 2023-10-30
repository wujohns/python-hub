import time
import asyncio
import concurrent.futures

# 处理方法
def run(index):
  time.sleep(2)
  print(f'index: { index }')

# 支持协程(事件轮询)运行的方法
async def run_tasks():
  with concurrent.futures.ProcessPoolExecutor(max_workers=4) as pool:
    tasks = []
    loop = asyncio.get_running_loop()
    for i in range(30):
      # 这里所作的操作即为将其他独立进程中的任务接入到事件轮询中
      task = loop.run_in_executor(pool, run, i)
      tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == "__main__":
  loop = asyncio.new_event_loop()
  loop.create_task(run_tasks())

  print('--------------')     # 可以看见这里直接先输出，上述的异步任务按照其执行的结果慢慢输出
  loop.run_forever()
