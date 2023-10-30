# 并行运行概述
这里主要针对在使用 python 解决并行任务的场景，针对这些场景，这里进行汇总和整理，以便于后续开发的参考

## 进程/线程/协程 简要说明

## 进程使用场景

## 线程使用场景

## 协程使用场景

## 技术决策范式
### 需要额外创建 进程/线程 场景
1. 对于进程和线程的治理，这里采用 concurrent.futures 的 线程池/进程池 方案  
1. 其采用方式为在全局维护一个 ProcessPoolExecutor 或 ThreadPoolExecutor (即线程池/进程池) 供业务逻辑进行使用  

### 纯IO负载场景
TODO 先完成 asyncio 的相关整理  

备注说明:  
1. 传统的进程管理方案为 multiprocessing  
1. 传统的线程管理方案为 threading  
1. concurrent.futures 模块实现了对threading(线程)和multiprocessing(进程)的更高级的抽象，对编写线程池/进程池提供了直接的支持  
1. 使用 concurrent.futures 模块，我们可以将相应的tasks直接放入线程池/进程池，不需要维护Queue来操心死锁的问题，线程池/进程池会自动帮我们调度  
1. concurrent.futures 提供的 submit 封装天然适配 asyncio 的接入  

## 实践参考
