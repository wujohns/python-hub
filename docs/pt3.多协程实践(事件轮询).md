# pt3 多协程实践(事件轮询)
这里主要使用 python 自带的事件轮询封装 asyncio

## 原理简要说明
1. 使用 asyncio 可在当前的线程中创建一个事件轮询(loop)  
1. 该 loop 会轮询检查其上的异步任务是否完成，若完成则继续后续的执行  

## 注意事项
1. 一个线程中只有一个 event_loop  
1. 在 async 函数外使用 get_event_loop 获取该 loop 对象  
1. 在 async 函数内使用 get_running_loop 获取该 loop 对象  

## 相关案例
1. 基础案例: [pt-demo/3.1.asyncio.py](/pt-demo/3.1.asyncio.py)  
1. fastapi 中自定义轮询 check: [pt-demo/asyncio-fastapi.py](/pt-demo/asyncio-fastapi.py)  

## 工程上的应用
1. 用在异步 io 类的任务处理中  
