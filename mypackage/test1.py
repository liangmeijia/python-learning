#引入模块时，会自动执行该模块对应的py文件。

#引入模块的方式1
# import test0 as t
#
# t.fun1()

#引入模块的式2
from mypackage.test0 import fun1
fun1()