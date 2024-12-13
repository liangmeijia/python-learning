import threading
import time
from  threading import Lock
"""
【进程】：是操作系统进行资源分配的基本单位，每打开一个程序至少就会有一个进程
【线程】是cpu调度的基本单位，每一个进程至少都会有一个线程，这个线程通常就是我们所说的主线程
一个进程默认有一个线程，进程里面可以创建多个线程，线程是依附在进程里面的，没有进程就没有线程。
【多线程】：是处理多任务的一种解决方式
【如何使用多线程】
1.导入线程模块 import threading
2.Thread线程类参数：target:执行的任务名；args：元组的形式给任务传参；kwargs：以字典的形式给任务传参
"""
# def sing():
#     print('我开始唱歌了')
#     time.sleep(2) #睡眠，以秒为单位
#     print('唱歌结束了')
# def play():
#     print('我开始玩游戏了')
#     time.sleep(2)
#     print('游戏结束了')
# if __name__ == '__main__':
#     #方式1：sing和play方法是依次先后执行
#     # sing()
#     # play()
#     #方式2：在主线程中开启子线程
#     t1 = threading.Thread(target=sing)
#     t2 = threading.Thread(target=play)
#     #守护线程：必须放在start方法前面，代表主线程执行完毕后，子线程也会结束
#     # t1.daemon = True
#     # t2.daemon = True
#     t1.start()
#     t2.start()
#     #阻塞主线程线程：必须放在start方法后面，代表子线程执行完毕后，主线程才会结束
#     t1.join()
#     t2.join()
#     #获取子线程名称
#     print(t1.name, t2.name)
#     #修改子线程名称
#     t1.name = '子线程1'
#     t2.name = '子线程2'
#     print(t1.name, t2.name)
#     print('完美闭幕')

'''
多线程的特点：
1、线程之间执行的顺序是无序的
2、线程之间共享资源（全局变量）
3、资源竞争
'''
# #案例1
# def fun(n):
#     time.sleep(2)
#     print(f'当前的线程是：{threading.current_thread().name},参数是{n}')
# #案例2
# li = [] #全局变量，共享的数据
# def wdata(n):
#     for i in range(n):
#         li.append(i)
#         time.sleep(1)
#     print(f'写入的数据是{li}')
# def rdata():
#     print(f'读出的数据是{li}')
# #案例3
# a = 0
# b = 1000000
# def add():
#     global a
#     for i in range(b):
#         a += 1
#     print(f'第一次累加是：{a}')
# def add2():
#     global a
#     for i in range(b):
#         a += 1
#     print(f'第二次累加是：{a}')
#if __name__ == '__main__':
#     # 1.无序
#     # for i in range(5):
#     #     t = threading.Thread(target=fun,args=(i,))
#     #     t.start()
#     #2.资源共享
#     wd = threading.Thread(target=wdata, args=(5,))
#     rd = threading.Thread(target=rdata, args=())
#     wd.start()
#     # 方式1 ：使用时间匹配
#     #time.sleep(5)
#     # 方式2：使用join
#     wd.join() #等写入数据的子线程执行完毕后，再执行读数据的线程
#     rd.start()
#     # 3.资源竞争
#     # add()
#     # add2()
#     t1 = threading.Thread(target=add)
#     t2 = threading.Thread(target=add2)
#     t1.start()
#     t2.start()
'''
【线程同步】（解决资源竞争，实际上就是变成单任务执行）
1.线程阻塞：使用join
2.同步锁：对共享数据进行锁定，保证多个线程访问共享数据不会出现数据错误问题:保证同一时刻只能有一个线程去操作。
注意：上锁和释放锁必须成对出现，否则容易造成死锁线程
'''
# a = 0
# b = 1000000
# lock = Lock() #全局同步锁
# def add():
#     lock.acquire() #上锁
#     global a
#     for i in range(b):
#         a += 1
#     print(f'第一次累加是：{a}')
#     lock.release() # 解锁
# def add2():
#     lock.acquire()  # 上锁
#     global a
#     for i in range(b):
#         a += 1
#     print(f'第二次累加是：{a}')
#     lock.release()  # 解锁
# if __name__ == '__main__':
#     # 3.资源竞争
#     # add()
#     # add2()
#     t1 = threading.Thread(target=add)
#     t2 = threading.Thread(target=add2)
#     t1.start()
#     #1.使用join
#     #t1.join()
#     t2.start()