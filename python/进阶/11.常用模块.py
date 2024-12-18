import os
import sys
import time
import logging
import random
'''
os:用于和操作系统进行交互
1.获取平台信息
2.对目录的操作
3.判断操作
'''
#1、指示正在使用的工作平台(返回操作系统类型) ;对于Windows,返回nt，对于Linux,返回posix
#print(os.name)

#2、把目录名和文件名分离，以元组的形式接收，第一个元素是目录路径，第二个元素是文件名
#print(os.path.split(r'D:\code\python\python-learning\python\进阶\11.常用模块.py'))

# 3、获取环境变量
#print(os.getenv('path'))

# 4、os.path.dirname 显示split分割的第一个元素，即目录
#print(os.path.dirname(r'D:\code\python\python-learning\python\进阶\11.常用模块.py'))

# 5、os.path. basename 显示split分割的第二个元素，即文件名
# print(os.path.basename(r'D:\code\python\python-learning\python\进阶\11.常用模块.py'))
# print(os.path.basename(r'D:\code\python\python-learning\python\进阶/'))

# 6、判断目录或者文件是否存在
# print(os.path.exists(r'D:\code\python\python-learning\python\进阶\11.常用模块.py'))

#7、判读是否是文件
# print(os.path.isfile(r'D:\code\python\python-learning\python\进阶'))
# print(os.path.isfile(r'D:\code\python\python-learning\python\进阶\11.常用模块.py'))

#8、判读是否是目录
# print(os.path.isdir(r'D:\code\python\python-learning\python\进阶/'))
# print(os.path.isdir(r'D:\code\python\python-learning\python\进阶\11.常用模块.py'))

#9、获取当前路径下的绝对路径
# print(os.path.abspath(''))
# print(os.path.abspath('11.常用模块.py'))

'''
sys :负责程序跟python解释器的交互
1.sys.getdefaultencoding(): 获取系统默认编码格式
2.sys.path: 获取环境变量的路径，跟解释器相关
3.sys.platform: 获取操作系统平台名称
4.sys.version: 获取python解释器的版本信息
'''

# 1、
# print(sys.getdefaultencoding())
# # 以列表的形式返回，第一项为当前所在的工作目录
# print(sys.path)
# print(sys.platform)
# print(sys.version)

'''
time: 3种时间表示
1、时间戳(timestamp) 是float类型，以秒为单位，距离1970-1-1 00:00:00 的时间差
2、时间元组(struct_time)
3、格式化的时间字符串(format time)
4、自定义格式化的时间字符串
'''

# print(12)
# time.sleep(2) #延时操作，以秒为单位
# print(34)

# # 获取当前时间戳
# print(f'系统当前时间戳是： {time.time()}')
# # 获取系统当前时间；将一个时间戳转换为当前时区的struct_time,九个元素
# print(f'系统当前结构化时间元组是： {time.localtime()}')
# struct_time = time.localtime(1734507546.5691803)
# print(struct_time)
# #print(struct_time.tm_year) #获取其中的tm_year元素
# # 获取系统当前时间；将一个时间元组转换为固定格式的字符串
# print(f'系统当前固定格式的时间字符串是： {time.asctime()}')
# str_time = time.asctime(struct_time)
# print(str_time)
# # 将一个时间戳转换为固定格式的字符串
# print(time.ctime(1734507546.5691803))
# # 将时间元组转换为 自定义格式的时间字符串
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# # 将自定义格式的时间字符串转换为 时间元组
# print(time.strptime('2023-10-09 12:00:09', '%Y-%m-%d %H:%M:%S'))

'''
logging:用于记录日志信息
1.程序调试
2.了解软件程序运行情况是否正常
3.软件程序运行故障分析与问题定位

级别排序(从高到低)：CRITICAL>ERROR>WARNING>INFO>DEBUG>OTES
'''
# logging.debug('debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')
#logging默认的level就warning,也就是说logging只会显示级别大于等于warning的日志信息

#修改logging的一些默认配置信息 logging.basicConfig() 配置root logger的参数
# 1.filename:指定日志文件的文件名。所有会显示的日志都会存放到这个文件中去
# 2.filemode:文件的打开方式，默认是a,追加模式
# 3.level:指定目志显示级别，默认是警告信息warning
# 4.format: 日志的输出格式
# logging.basicConfig(filename='log.log',
#                     filemode='a',
#                     level=logging.DEBUG,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',encoding='utf-8')
#
# logging.debug('哈哈哈debug')
# logging.info('info')
# logging.warning('warning')
# logging.error('error')
# logging.critical('critical')
'''
random:用于实现各种分布的伪随机数生成器，可以根据不同的实数分布来随机生成值
'''
#产生大于0且小于1之间的【小数】
print(random.random())
#产生指定范围的随机【小数】
print(random.uniform(1, 3))
#产生指定范围内的随机【整数】，包括开头和结尾
print(random.randint(1, 4))
#产生start，stop范围内的随机整数，包含开头但是不包含结尾
#指定产生随机的步长step，随机选择一个数据
print(random.randrange(2,5,2)) # 2，4
