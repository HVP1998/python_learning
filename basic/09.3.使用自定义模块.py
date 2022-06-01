# 含有空格或以数字开头的文件利用__import__("文件名")引入
__import__("09.2.自定义模块")
import demo
p=demo.Person("十大奇",demo.GENDER.女,18)
p.SayHi()
print(demo.__doc__)
