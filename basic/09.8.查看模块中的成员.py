# dir()方法可以查看一个模块中外部可访问的成员与外部不可访问成员(带有双下划线修饰的私有成员)
import string
print(dir(string))
print([element for element in dir(string) if not element.startswith("__")])
# 使用__all__变量，也可以直接查看模块，但不是所有的模块都支持__all__属性
print(string.__all__)