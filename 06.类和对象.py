# # 定义类
# class Person:
#     #构造函数   
#     def __init__(self,name,age,gender):
#         print("my name is",name,"my gender is",gender,"and I am ",age)
# p=Person("James Bond",35,'man')


# # 类对象的创建与使用
# class Person:
#     name="..."
#     gender="."
#     age=0
#     def __init__(self,name,gender,age):
#         self.name=name
#         self.gender=gender
#         self.age=age
# # 增加实例变量
# Person.career="***"
# Person.id="***********"
# # 动态增加方法
# def SayHi(self):
#     print("My name is",self.name,"and I am ",self.age)
# Person.SayHello=SayHi
# Person.SayHello(Person)
# # 利用lambda表达式动态增加方法
# Person.MyCareer=lambda self:print("My career is",self.career)
# Person.MyCareer(Person)
# # 利用MethodType动态增加方法
# from types import MethodType
# def MyId(self):
#     print("My Id is",self.id)
# Person.MyId=MethodType(MyId,Person)
# p1=Person("Kachy",'man',23)
# p1.career="hunter"
# p1.id="2162530213"
# p1.SayHello()
# p1.MyCareer()
# p1.MyId()


# # 类变量和实例变量 类方法和实例方法、静态方法
# # class CLanguage:
# #     # 类变量    类内方法以外
# #     name="C语言中文网"
# #     address="http://c.biancheng.net"
# #     # 实例方法
# #     def say(self,content):
# #         print("the conten:",content)
# # print(CLanguage.name)
# # print(CLanguage.address)
# # CLanguage.name="python教程"
# # CLanguage.address="http://c.biancheng.net/python"
# # print(CLanguage.name)
# # print(CLanguage.address)
# # print("修改前，各类对象中类变量的值：")
# # clang1 = CLanguage()
# # print(clang1.name)
# # print(clang1.add)
# # clang2 = CLanguage()
# # print(clang2.name)
# # print(clang2.add)
# # print("修改后，各类对象中类变量的值：")
# # CLanguage.name = "Python教程"
# # CLanguage.add = "http://c.biancheng.net/python"
# # print(clang1.name)
# # print(clang1.add)
# # print(clang2.name)
# # print(clang2.add)
# class CLanguage:
#     # 类构造函数也属于实例方法
#     def __init__(self,name,address):
#         # 实例变量  类体中方法内以self.arg定义的变量
#         self.name=name
#         self.address=address
#     def say(self):
#         print(self.calaog)
#     def test(self):
#         # 局部变量
#         whole=self.name+"\t"+self.address
#         return whole
#     # 和实例方法类似
#     @classmethod
#     def classfun(cls):
#         print("这是一个类方法",cls)
#     # 静态方法没有任何绑定所以不能使用类属性或类方法
#     @staticmethod
#     def staticfun(name,address):
#         print(name,address)
# # 创建两个类对象
# clang1=CLanguage("python教程","http://c.biancheng.net/python/")
# clang2=CLanguage("C语言教程","http://c.biancheng.net/c/")
# print(clang1.name)
# print(clang1.address)
# print(clang2.name)
# print(clang2.address)
# # 通过类对象不能影响类变量   因为类对象改变变量的值不是为类变量赋值而是定义新的实例变量
# # 改变当前类对象的实例变量不会影响其他类对象的实例变量
# # 实例变量可与类变量同名，此时通过类调用变量时优先调用实例变量
# clang1.name="C++教程"
# clang1.address="http://c.biancheng.net/cplus/"
# print(clang1.name)
# print(clang1.address)
# print(clang2.name)
# print(clang2.address)


# 实例方法
class CLanguage:
    def info(self):
        print(self,"正在学 Python")
#通过类名直接调用实例方法
CLanguage.info("zhangsan")
