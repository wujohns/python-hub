# 并行运行概述
这里主要针对在使用 python 解决并行任务的场景，针对这些场景，这里进行汇总和整理，以便于后续开发的参考

## 进程/线程/协程 简要说明
1. 进程是操作系统分配的独立执行单元，每个进程都有自己的独立内存空间、代码、数据和系统资源  
1. 线程是进程内的执行单元，多个线程可以共享同一个进程的内存空间和资源  
1. 协程是代码层面上实现的执行单元，其通过事件轮询机制提供更便捷的并发任务管理  

## 技术决策范式
### 需要额外创建 进程/线程 场景
1. 对于进程和线程的治理，这里采用 concurrent.futures 的 线程池/进程池 方案  
1. 其采用方式为在全局维护一个 ProcessPoolExecutor 或 ThreadPoolExecutor (即线程池/进程池) 供业务逻辑进行使用  
1. 需要异步执行的场景采用 submit 的调用方式  

详细可以参考:  
多进程异步案例: [pt-demo/1.3.multiprocessing-submit.py](/pt-demo/1.3.multiprocessing-submit.py)  
多线程异步案例: [pt-demo/2.3.threading-submit.py](/pt-demo/2.3.threading-submit.py)  
多线程异步调用 async 函数案例: [pt-demo/plus.asyncio-threading.py](/pt-demo/plus.asyncio-threading.py)  

### 纯IO负载场景
1. 对于 fastapi 这类本身支持 async/await 模式的框架，直接使用其框架推荐处理方式即可  
1. 对于需要自建定时监听并执行任务，可以程序初始化时使用 asyncio.get_event_loop() 获取对应的 loop 对象，然后通过 loop.create_task 的方式创建对应的监听处理  

详细可以参考:  
1. fastapi 中自定义轮询 check: [pt-demo/asyncio-fastapi.py](/pt-demo/asyncio-fastapi.py)  

其他备注说明:  
1. 传统的进程管理方案为 multiprocessing  
1. 传统的线程管理方案为 threading  
1. concurrent.futures 模块实现了对threading(线程)和multiprocessing(进程)的更高级的抽象，对编写线程池/进程池提供了直接的支持  
1. 使用 concurrent.futures 模块，我们可以将相应的tasks直接放入线程池/进程池，不需要维护Queue来操心死锁的问题，线程池/进程池会自动帮我们调度  
1. concurrent.futures 提供的 submit 封装天然适配 asyncio 的接入  

## 一些参考
uvloop 相关: https://juejin.cn/post/7113535203879944223
