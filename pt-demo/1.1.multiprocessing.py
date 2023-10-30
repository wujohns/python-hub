# 多进程处理
import time
import concurrent.futures

# 处理方法
def run(index):
  time.sleep(2)
  return index

if __name__ == "__main__":
  with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
    futures = []
    for i in range(30):
      future = executor.submit(run, i)
      futures.append(future)

    print('并行任务批量提交完毕，等待执行')
    for future in concurrent.futures.as_completed(futures):
      print(f'return: { future.result() }')
    print('任务执行完毕')

# 更友好的展示
# from tqdm import tqdm
# if __name__ == "__main__":
#   with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
#     futures = []
#     for i in range(30):
#       future = executor.submit(run, i)
#       futures.append(future)

#     result_list = tqdm(
#       concurrent.futures.as_completed(futures),
#       desc=u'已完成0个task'
#     )
#     finished_index = 0
#     for result in result_list:
#       finished_index += 1
#       result_list.set_description(f'已完成{ finished_index }个task')
