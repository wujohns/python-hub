import concurrent.futures

# 创建全局进程池
executor = concurrent.futures.ProcessPoolExecutor(max_workers=4)

# 处理方法
def run(index):
  # 3000万次轮询
  for _ in range((10**7)*3):
    a = 'aa'
  print(f'index: { index }')

if __name__ == '__main__':
  for i in range(30):
    executor.submit(run, i)
  
  print('-----------')
