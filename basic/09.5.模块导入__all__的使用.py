# 导入模块有三种方法：
# 1.import 模块名               模块名.成员
# 2.from 模块名 import 成员名    成员名
# 3.from 模块名 import *        成员名
# __all__是一个列表其中元素表示在第三种模块导入方法中可以被使用的模块成员
from demo import *
import sys
p=Person("张三",GENDER.男,28)
Introduce()
