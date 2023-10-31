# pt1 多进程实践
这里主要采用 concurrent.futures 中的线程池方案来维护治理多线程的使用  

## 原理简要说明
1. 从当前运行的进程中创建新的线程并维护

## 基础案例
参考 [pt-demo/2.1.threading.py](/pt-demo/2.1.threading.py)  

## 异步多任务
这里主要提供了两种异步策略:  
1. 使用将其接入事件轮询，该方式可以较好的配合当前采用协程作为底座的框架，参考 [pt-demo/2.2.threading-async.py](/pt-demo/2.2.threading-async.py)  
1. 使用 submit 模式，该方式为传统方式，参考 [pt-demo/2.3.threading-submit.py](/pt-demo/2.3.threading-submit.py)  

## 工程上的应用
1. 需要在执行上做隔离场景，避免单处cpu阻塞造成整体阻塞  
1. 相比与多进程方案，多线程可以方便共享全局变量  
1. 在引入协程处理方案后，线程方案比较鸡肋  
