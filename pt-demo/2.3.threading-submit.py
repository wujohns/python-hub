import concurrent.futures
import time

# 创建全局进程池
executor = concurrent.futures.ThreadPoolExecutor(max_workers=40)

# 处理方法
def run(index):
  # 3000万次轮询
  # for _ in range((10**7)*3):
  #   a = 'aa'
  time.sleep(2)
  print(f'index: { index }')

if __name__ == '__main__':
  for i in range(30):
    executor.submit(run, i)

  print('-----------')