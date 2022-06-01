# __file__属性可以得到包的绝对路径，但是对于不是用python语言学写的包就无法使用
import my_package
print(my_package.__file__)