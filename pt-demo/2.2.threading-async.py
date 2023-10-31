import asyncio
import concurrent.futures
import time

# 创建全局线程池
executor = concurrent.futures.ThreadPoolExecutor(max_workers=40)

# 处理方法
def run(index):
  # 3000万次轮询
  # for _ in range((10**7)*3):
  #   a = 'aa'
  time.sleep(2)
  print(f'index: { index }')

# 支持协程(事件轮询)运行的方法
async def run_tasks():
  tasks = []
  loop = asyncio.get_running_loop()
  for i in range(30):
    # 这里所作的操作即为将其他独立进程中的任务接入到事件轮询中
    task = loop.run_in_executor(executor, run, i)
    tasks.append(task)

  # gather -- 整体失败
  # wait -- 单独控制
  await asyncio.gather(*tasks)
  # await asyncio.wait(tasks)

if __name__ == "__main__":
  loop = asyncio.new_event_loop()
  loop.create_task(run_tasks())
  loop.create_task(run_tasks())

  print('--------------')     # 可以看见这里直接先输出，上述的异步任务按照其执行的结果慢慢输出

  # 保持程序不退出
  loop.run_forever()
