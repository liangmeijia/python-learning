import time
from multiprocessing import Process
import threading
import os
from queue import Queue
"""
【进程】
1.含义：
是操作系统进行资源分配和调度的基本单位，是操作系统结构的基础；
一个正在运行的程序或者软件就是一个进程；
程序跑起来就成了进程；
注意:进程里面可以创建多个线程，【多进程也可以完成多任务】
2.状态
2.1.就绪状态:运行的条件都已经满足，正在等待cpu执行
2.2.执行状态:cpu正在执行其功能
2.3.等待(阻塞)状态: 等待某些条件满足，如一个程序sleep了，此时就处于等待状态
"""

'''
进程语法结构
1.导入模块
multiprocessing模块提供了Process类代表进程对象
2. Process 类参数
target:执行的目标任务名，即子进程要执行的任务
args:以元组的形式传参
kwargs:以字典的形式传参
3.常用的方法
start():开启子进程
is_alive():判断子进程是否还活着，存活返回True,死亡返回False
join():阻塞线程，主进程等待子进程执行结束
4. 常用的属性
name:当前进程的别名。默认Process-N
pid:当前进程的进程编号
'''
# def sing():
#     print(f'sing子进程pid ：{os.getpid()}') #获取当前进程的pid
#     print(f'sing父进程pid ：{os.getppid()}') #获取当前进程的父进程pid
#     print('唱歌')
# def dance():
#     print(f'dance子进程pid ：{os.getpid()}')  # 获取当前进程的pid
#     print(f'dance父进程pid ：{os.getppid()}')  # 获取当前进程的父进程pid
#     print('跳舞')
#
# if __name__ == '__main__': #主进程
#     #开启子进程
#     p1 = Process(target=dance,name='dance')
#     p2 = Process(target=sing,name='sing')
#     p1.start()
#     p2.start()
#     print(f'p1的name是{p1.name}')
#     print(f'p2的name是{p2.name}')
#     print(f'主进程pid是{os.getpid()}')
#     print(f'主进程的父进程pid是{os.getppid()}')

# def eat(name):
#     print(f'{name}在吃饭')
# def sleep(name):
#     print(f'{name}在睡觉')
# if __name__ == '__main__':
#     # p1 = Process(target=eat,args=('alice',))
#     # p2 = Process(target=sleep,args=('alice',))
#     p1 = threading.Thread(target=eat,args=('alice',))
#     p2 = threading.Thread(target=sleep,args=('alice',))
#     p1.start()
#     p2.start()
#     print('哈哈哈')
#     print(f'p1:{p1.is_alive()}')
#     print(f'p2:{p2.is_alive()}')
#     # 总结：
#     # 主进程会先于子进程运行

#进程之间资源不共享
# li = [] #全局变量
# def wdata(n):
#     for i in range(n):
#         li.append(i)
#         #time.sleep(1)
#     print(f'写入的数据是{li}')
# def rdata():
#     print(f'读出的数据是{li}')
# if __name__ == '__main__':
#     p1 = Process(target=wdata, args=(6,))
#     p2 = Process(target=rdata, args=())
#     p1.start() # 可以正确地写入数据
#     #p1.join()
#     p2.start() #读出的数据是空的，因为进程间不共享全局变量
#     print('哈哈哈')
#     print(f'p1:{p1.is_alive()}')
#     print(f'p2:{p2.is_alive()}')
'''
进程间的通信（使用队列Queue）
q = Queue(n)：初始化一个队列，n如果是负数或0就代表Queue队列的数据个数没有限制，直到内存的上限
q.put():放入数据
q.get():取出数据
q.empty(): 判断队列是否为空
q.qsize():返回当前队列包含的消息数量
q.fu11():判断队列是否满了
'''
li = [] #全局变量
def wdata(n,q):
    for i in range(n):
        li.append(i)
        q.put(i)
        time.sleep(1)
    print(f'写入的数据是{li}')
def rdata(q):
    while not q.empty():
        return q.get()
    print(f'读出的数据是{li}')
if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=wdata, args=(4,q))
    p2 = Process(target=rdata, args=(q,))
    p1.start() # 可以正确地写入数据
    #p1.join()
    p2.start() #读出的数据是空的，因为进程间不共享全局变量

