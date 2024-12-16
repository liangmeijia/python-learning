from greenlet import greenlet
import gevent
import time
'''
协程:单线程下的开发，又称为微线程
实现：利用生成器 yield关键字
注意:协程的切换是由程序员显式控制的，而不是由操作系统调度
应用场景：如y果一个线程里面I0（Input/Output）操作比较多的时候，可以用协程；适合高并发处理
常见的I0操作:文件操作、网络请求
'''

'''
greenlet:是一个由C语言实现的协程模块。通过设置switch()来实现任意函数之间的切换
注意:greenlet属于【手动切换】，当遇到I0操作，程序会阻塞，而不能进行自动切换
'''

# def sing():
#     print('21在唱歌')
#     g2.switch()  # 通过switch（）方法实现不同任务间的切换
#     print('22唱完歌了')
#
# def dance():
#     print('11在跳舞')
#     g1.switch()
#     print('12跳完舞了')
#
# if __name__ == '__main__':
#     g1 = greenlet(sing) #创建协程对象
#     g2 = greenlet(dance)
#     g2.switch()

'''
gevent：遇到I0操作时，会进行【自动切换】，属于主动式切换
gevent.spawn(函数名):创建协程对象
gevent.sleep():耗时操作
gevent.join():阻塞，等待某个协程执行结束
gevent.joinall()：等待所有协程对象都执行结束再退出，参数是一个协程对象列表


'''
def sing():
    print('在唱歌')
    print('唱完歌了')

def dance():
    print('在跳舞')
    time.sleep(6)
    print('跳完舞了')

if __name__ == '__main__':
   g1 = gevent.spawn(sing)
   g2 = gevent.spawn(dance)
   g1.join()
   #g2.join()