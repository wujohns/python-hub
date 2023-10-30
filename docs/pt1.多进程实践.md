# pt1 多进程实践
这里主要采用 concurrent.futures 中的进程池方案来维护治理多进程的使用  

## 原理简要说明
1. concurrent.futures 通过调用操作系统 fork 的方式创建一个和父进程几乎完全相同的子进程，这个子进程从父进程复制了代码、数据、堆栈等  
1. 子进程在创建时独立运行，拥有自己的内存空间和 Python 解释器  

## cpu 密集型的单次多任务
参考 [pt-demo/1.1.multiprocessing.py](/pt-demo/1.1.multiprocessing.py)  

## cpu 密集型的异步多任务
参考 [pt-demo/1.2.multiprocessing-async.py](/pt-demo/1.2.multiprocessing-async.py)  

## 注意事项
1. 在 win 下多进程的调用需要放在 __main__ 下  
1. 由于 concurrent.futures 的 fork 策略，在新建进程中调用的方法需要为在对应的 pool 之前定义好的方法(否则会出现找不到对应函数的报错)  

## 工程上的应用
如果需要在持续运行的服务中使用多进程，则需要遵守以下规范:  
1. pool 的创建需要放在其他模块的初始化之后或放在其依赖的模块的初始化之后  
1. 需要按照上述异步多任务的方式调度多进程，避免对主进程造成阻塞  
