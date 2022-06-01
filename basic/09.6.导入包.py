# 导入包有三种方法
# 1.import 包名 
# 2.import 包名.模块名  
# 3.from 包名 import 模块名  
# 4.from 包名.模块名 import 成员名  
# 5.这里需要注意使用第一种方法只是导入并执行包下的__init__.py文件
import my_package
print(my_package)
print(my_package.__doc__)
print(type(my_package))
from my_package.demo1 import Person as person
from my_package.demo1 import GENDER as gender
p=person("王家宝",gender.男,22)
p.SayHi()
