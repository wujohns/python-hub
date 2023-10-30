# 多线程处理
# 该部分主要可以和 1.1.multiprocessing.py 进行对比
import time
import concurrent.futures

# 创建全局线程池
executor = concurrent.futures.ThreadPoolExecutor(max_workers=40)

# 处理方法
def run(index):
  for _ in range((10**7)*3):
    a = 'aa'
  return index

if __name__ == "__main__":
  start = time.time()
  futures = []
  for i in range(30):
    future = executor.submit(run, i)
    futures.append(future)

  print('并行任务批量提交完毕，等待执行')
  for future in concurrent.futures.as_completed(futures):
    print(f'return: { future.result() }')
  print('任务执行完毕')
  print(f'cost time: { time.time() - start }')
