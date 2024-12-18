from greenlet import greenlet
import gevent
import time
from gevent import monkey
'''
协程:单线程下的开发，又称为微线程
实现：利用生成器 yield关键字
注意:协程的切换是由程序员显式控制的，而不是由操作系统调度
应用场景：如果一个线程里面I0（Input/Output，文件操作，网络爬虫请求）操作比较多的时候，可以用协程；适合高并发处理
常见的I0操作:文件操作、网络请求
'''

'''
greenlet:是一个由C语言实现的协程模块。通过设置switch()来实现任意函数之间的切换
注意:greenlet属于【手动切换】，当遇到I0操作，程序会阻塞，而不能进行自动切换
'''

# def sing():
#     print('在唱歌')
#     time.sleep(2)
#     g2.switch()  # 通过switch（）方法实现不同任务间的切换
#     print('唱完歌了')
#
# def dance():
#     print('在跳舞')
#     g1.switch()
#     print('跳完舞了')
#
# if __name__ == '__main__':
#     g1 = greenlet(sing) #创建协程对象
#     g2 = greenlet(dance)
#     g2.switch()

'''
gevent：遇到I0操作时，会进行【自动切换】任务，属于主动式切换
gevent.spawn(函数名):创建协程对象
gevent.sleep():耗时操作
gevent.join():阻塞，等待某个协程执行结束
gevent.joinall()：等待所有协程对象都执行结束再退出，参数是一个协程对象列表


'''
# def sing():
#     print('在唱歌')
#     # time.sleep(3)
#     gevent.sleep(1) #使用gevent的sleep（）方法，会自动切换协程；使用time.sleep()就不会自动切换
#     print('唱完歌了')
#
# def dance():
#     print('在跳舞')
#     # time.sleep(6)
#     gevent.sleep(6)
#     print('跳完舞了')
#
# if __name__ == '__main__':
#     # 1.创建协程对象
#    g1 = gevent.spawn(sing)
#    g2 = gevent.spawn(dance)
#     # 2.阻塞，等待协程执行完毕
#     # 如果只写了g1.join()，没写g2.join()，g2耗时操作后面的代码可能不会被执行
#    g1.join()
#    g2.join()
'''
结果:
在唱歌
在跳舞 
唱完歌了
跳完舞了
解释：
在唱歌和在跳舞是同时执行的
然后等1s后执行唱完歌了，再等5秒执行跳完舞了
'''
#monkey.patch_all() #将用到的time.sleep()代码替换成gevent.sleep()代码
#注意:monkey.patch_al1()必须放在被打补丁者的前面
def sing(name):
    for i in range(5):
        time.sleep(1)
        #gevent.sleep(1)
        print(f'{name}在第{i}个舞台上唱歌')
if __name__ == '__main__':
    gevent.joinall(
       [
           gevent.spawn(sing, '波波'),
           gevent.spawn(sing, '糖糖')
       ]
    )
'''
【总结】
进程、线程和协程对比：
1、
线程是CPU调度的基本单位
进程是os资源分配的基本单位
协程是线程下的开发，是微线程
2、
进程:切换需要的资源最大，效率最低
线程:切换需要的资源一般，效率一般
协程:切换需要的资源最小，效率高
3、
多线程适合I0密集型操作(文件操作、爬虫)
多进程适合CPU密集型操作(科学及计算、对视频进行高清解码、计算圆周率)
4、
协程的切换是由程序员显式控制的，线程和进程是由操作系统调度
5、
进程、线程协程都是可以完成多任务的，可以根据自己实际开发的需要选择使用。
'''