# # 定义类
# class Person:
#     #构造函数   
#     def __init__(self,name,age,gender):
#         print("my name is",name,"my gender is",gender,"and I am ",age)
# p=Person("James Bond",35,'man')

# ****************************************************************************************

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
# Person.MyID=MethodType(MyId,Person)
# p1=Person("Kachy",'man',23)
# p1.career="hunter"
# p1.id="2162530213"
# p1.SayHello()
# p1.MyCareer()
# p1.MyID()

# ****************************************************************************************

# # # 类变量和实例变量 类方法和实例方法、静态方法
# # #类体中、所有函数之外：此范围定义的变量，称为类属性或类变量；
# # #类体中，所有函数内部：以“self.变量名”的方式定义的变量，称为实例属性或实例变量；
# # #类体中，所有函数内部：以“变量名=变量值”的方式定义的变量，称为局部变量
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
# # print(clang1.address)
# # clang2 = CLanguage()
# # print(clang2.name)
# # print(clang2.address)
# # print("修改后，各类对象中类变量的值：")
# # CLanguage.name = "Python教程"
# # CLanguage.address = "http://c.biancheng.net/python"
# # print(clang1.name)
# # print(clang1.address)
# # print(clang2.name)
# # print(clang2.address)
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

# ****************************************************************************************

# # 实例方法、静态方法、类方法的辨析
# class CLanguage:
#     def info1(self):
#         print(self,"正在学 Python")
#     @classmethod
#     def info2(cla):
#         print(cla,"正在学 Python")
#     @staticmethod
#     def info3(static):
#         print(static,"正在学 Python")
# #通过类名直接调用实例方法，此时不会自动给self传值，利用类调用类成员的方式称为非绑定方法
# CLanguage.info1("zhangsan")
# #通过实例对象调用实例方法，此时则会自动给self传值，利用实例对象访问类成员的方式称为绑定方式
# person=CLanguage()
# person.info1()
# person.info2()
# person.info3("zhangsan")

# ****************************************************************************************

# ## 描述符
# # class revealAccess:
# #     def __init__(self,arg,name):
# #         self._arg=arg
# #         self._name=name
# #     def _get_(self,arg,argtype):
# #         print("Retrieving",self._name)
# #         return self._arg
# #     def _set_(self,arg,name):
# #         print("Updating",self._name)
# #         self._name=name
# # class testClass:
# #     x=revealAccess(10,"var x")
# #     y=5
# # test=testClass()
# # print(test.x)
# # test.x=20
# # print(test.x)
# # print(test.y)
# class TestClass:
#     def __init__(self,arg):
#         print("creation complete")
#         self._arg=arg
#     def getter(self):
#         return self._arg
#     def setter(self,arg):
#         self._arg=arg
#     def deleter(self):
#         self._arg=None
#     argument=property(getter,setter,deleter,"the")
# test=TestClass(12)
# # 调用fdoc有两种方法
# # print(TestClass.argument.__doc__)
# help(TestClass.argument)
# # 调用getter
# print(test.argument)
# # 调用setter
# test.argument=21
# # 调用getter
# print(test.argument)
# # 调用deleter
# del test.argument
# # 调用getter
# print(type(test.argument))

# ****************************************************************************************

# # 私有属性
# class Person:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.__ID="**********"
#     def getid(self):
#         return self.__ID
#     def setid(self,value):
#         if isinstance(value,str):
#             raise TypeError("ID of People must not to be str!")
#         self.__ID=value
#     def delid(self):
#         self.__ID="**********"
# p1=Person("张三",18,"男")
# p1.setid(12345)
# # 当id设置为字符串则会报错
# # p1.setid("12345")
# print(p1.getid())
# # 打印id的内存地址
# print("ID的内存地址：",id(p1.getid()))
# # 如下的赋值不会改变原有私有属性只会创建一个实例属性并给其赋值
# # 证明如下得到的内存地址不同
# p1.__ID=98765
# print("__ID的内存地址：",id(p1.__ID))

# ****************************************************************************************

# # @property
# class Person():
#     def __init__(self,name,age,gender):
#         self.__name=name
#         self.__age=age
#         self.__gender=gender
    
#     @property
#     def name(self):
#         a=self.__name
#         a=a.replace(a[0],"*")
#         return a
#     @name.setter
#     def name(self,value):
#         if not isinstance(value,str):
#             raise TypeError("Name has to be str")
#         self.__name=value
#     @name.deleter
#     def name(self):
#         self.__name=None
    
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,value):
#         if not isinstance(value,int):
#             raise TypeError("age has to be int")
#         self.__age=value
#     @age.deleter
#     def age(self):
#         self.__age=None

#     @property
#     def gender(self):
#         return self.__gender
#     @gender.setter
#     def gender(self,value):
#         if not isinstance(value,str):
#             raise TypeError("Name has to be str")
#         self.__gender=value
#     @gender.deleter
#     def gender(self):
#         self.__gender=None
    
# p1=Person("瑪法里奧",23,"♂")
# p1.name="瑪法里奧.怒風"
# p1.age=35000
# p2=Person("伊利丹",22,"♂")
# p2.name="伊利丹.怒風"
# p2.age=30000
# print(p2.name,"對陣",p1.name)

# ****************************************************************************************
    
# # 私有属性、私有方法就是对类的数据进行了封装
# # 实际上私有成员也可在类的外部调用
# # 这是因为python在底部将私有成员的名臣改变了例如：person类中__name的实际名称是_person__name
# # 所以在类的外部调用私有成员的方式是：_类名__私有成员名
# class person:
#     def __init__(self,name,age):
#         self.__name=name
#         self.__age=age
#     def __showage(self):
#         print("我的年龄是：",self.__age)

# p=person("Jamse",18)
# print("my name is",p._person__name)
# p._person__showage()

# ****************************************************************************************

# # 继承
# 子类继承父类的公有属性、方法、私有属性、方法、构造函数
# # class 派生类(基类)   class 父类(子类)
# class Person(object):
#     def __init__(self,name0,age0,gender0):
#         self.__name=name0
#         self.__age=age0
#         self.__gender=gender0
#     @property
#     def name(self):
#         a=self.__name
#         a=a.replace(a[0],"*")
#         return a
#     @name.setter
#     def name(self,value):
#         if not isinstance(value,str):
#             raise TypeError("Name has to be str")
#         self.__name=value
#     @name.deleter
#     def name(self):
#         self.__name="***"
    
#     @property
#     def age(self):
#         if(self.__gender=="男"):
#             return self.__age
#         elif(self.__gender=="女"):
#             return "㊙"
#     @age.setter
#     def age(self,value):
#         if not isinstance(value,int):
#             raise TypeError("Age has to be int")
#         self.__age=value
#     @age.deleter
#     def age(self):
#         self.__age="∞"

#     @property
#     def gender(self):
#         return self.__gender
#     @gender.setter
#     def gender(self,value):
#         if not ((value=="男")or(value=="女")):
#             raise TypeError("Gender has to be 男 or 女.")
#         elif ((value=="boy")or(value=="girl")):
#             raise TypeError("This system is not support register gender in English.")
#         self.__gender=value
#     @gender.deleter
#     def gender(self):
#         self.__gender="?"
    
#     def SayHi(self):
#         print("我的名字是：",self.name,"我的性别是：",self.gender,"我的年龄是：",self.age)
#     def __secret(self):
#         print("this is my secret.")
# class Student(Person):
#     pass
# p=Person("木子",22,"女")
# p.SayHi()
# s=Student("李雷",18,"男")
# s.SayHi()
# s._Person__secret()
# print(issubclass(Student,Person))
# print(issubclass(Student,object))
# 继承不会继承doc属性

# ****************************************************************************************

# # 子类无构造方法默认调用父类构造方法
# class Book(object):
#     def __init__(self,name,price,category):
#         self._name=name
#         self._price=price
#         self._category=category
#     def showmsg(self):
#         print(self._name+"是"+self._category+"类图书"+"一本"+self._price)
# class Comic(Book):
#     pass
# c1=Comic("batman","23$","detective comic")
# # 子类有构造方法而且不显示调用父类的构造方法
# class MovieMagazine(Book):
#     def __init__(self, date):
#         self._date=date
# mm1=MovieMagazine("2021.11")
# # 由于没有显式调用父类的构造方法所以没有父类中的属性，所以如下语句会报错
# # print(m1._name)
# # 子类有构造方法而且显式调用父类的构造方法
# class CarMagazine(Book):
#     def __init__(self,name,price,category,date):
#         self._date=date
#         super(CarMagazine,self).__init__(name,price,category)
# cm1=CarMagazine("车行天下","23￥","杂志","2021.11")
# cm1.showmsg()
# # super还可用于一般重名方法的调用
# class FableStory(Book):
#     def __init__(self,name,price,category,date):
#         self._date=date
#         super(FableStory,self).__init__(name,price,category)
#     def showmsg(self):
#         super(FableStory,self).showmsg()
#         print("这本书是第"+self._date+"期")

# ****************************************************************************************

# # MRO解析
# # 不使用super而直接调用父类的初始化方法会多次调用
# class A(object):
#     def __init__(self):
#         print("--enter A")
#         print("--quite A")

# class B(A):
#     def __init__(self):
#         print("---enter B")
#         A.__init__(self)
#         print("---quite B")

# class C(A):
#     def __init__(self):
#         print("---enter C")
#         A.__init__(self)
#         print("---quite C")

# class D(C,B):
#     def __init__(self):
#         print("---enter D")
#         B.__init__(self)
#         C.__init__(self)
#         print("---quite D")  
# d=D()
# print("MRO：",[x.__name__ for x in D.__mro__ ])
# # # 而如果使用super则会由于python底层的MRO在实际调用的时候会根据其规定好的顺序进行调用
# # class A(object):
# #     def __init__(self):
# #         print("  --enter A")
# #         print("  --quite A")

# # class B(A):
# #     def __init__(self):
# #         print(" ---enter B")
# #         super(B,self).__init__()
# #         print(" ---quite B")

# # class C(A):
# #     def __init__(self):
# #         print(" ---enter C")
# #         super(C,self).__init__()
# #         print(" ---quite C")

# # class D(C,B):
# #     def __init__(self):
# #         print("----enter D")
# #         super(D,self).__init__()
# #         print("----quite D")
# # d=D()
# # print("MRO：",[x.__name__ for x in D.__mro__ ])

# ****************************************************************************************

# # 父类中的函数可以被子类重写，子类会直接调用重写的重名函数
# # 使用父类.函数()的形式可以调用父类中的重名函数
# class bird(object):
#     def __init__(self):
#         print("I am a bird")
#     def isWing(self):
#         print("I hava a pair wings")
#     def fly(self):
#         print("I can fly")
# class ostrich(bird):
#     def fly(self):
#         print("I can not fly")
# o=ostrich()
# o.fly()
# bird.fly(o)

# ****************************************************************************************

# # __slots__可以限制实例属性和实例方法的动态添加，但是对子类没有限制作用，只在当前类起作用
# # __slots__必须包括当前类中存在的属性和方法不然会报错
# class Person(object):
#     # 如果没有"_Person__name","_Person__gender","_Person__age"则将会报错如下
#     # 'Person' object has no attribute '_Person__name'
#     # __slots__=("ID","SayHi")
#     __slots__=("ID","SayHi","_Person__name","_Person__gender","_Person__age")
#     def __init__(self,name,gender,age):
#         self.__name=name
#         self.__gender=gender
#         self.__age=age
#     @property
#     def name(self):
#         a=self.__name
#         a=a.replace(a[0],"*")
#         return a
#     @name.setter
#     def name(self,value):
#         if not isinstance(value,str):
#             raise TypeError("name has to be str")
#         self.__name=value
#     @name.deleter
#     def name(self):
#         self.__name="***"

#     @property
#     def gender(self):
#         return self.__gender
#     @gender.setter
#     def gender(self,value):
#         if not isinstance(value,str):
#             raise TypeError("gender has to be str")
#         self.__gender=value
#     @gender.deleter
#     def gender(self):
#         self.__gender="*"

#     @property
#     def age(self):
#         if(self.__gender=="男"):
#             return self.__age
#         elif(self.__gender=="女"):
#             return "㊙"
#     @age.setter
#     def age(self,value):
#         if not isinstance(value,int):
#             raise TypeError("age has to be int")
#         self.__age=value
#     @age.deleter
#     def age(self):
#         self.__age="***"

# class Student(Person):
#     pass

# def sayhi(self):
#     print("Hello")

# p=Person("张三","男",22)
# p.SayHi=sayhi
# p.SayHi=sayhi(p)
# s=Student("李磊","女",16)
# s.SayHello=sayhi
# s.SayHello=sayhi(s)

# ****************************************************************************************

# # 动态创建类
# # type(类名,利用元组表示被继承的父类,利用字典动态增加实例函数与实例属性)
# # 如果字典中变量的赋值是普通数据则是实例属性，如果是函数则是实例函数

# class animle:
#     pass
# def showmsg(self):
#     print("I am an animle")
# animle=type("animle",(object,),dict(ShowMsg=showmsg,name="animle"))
# a=animle()
# a.ShowMsg()
# print(a.name)

# ****************************************************************************************

# # metacalss
# # 一般元类有两个必要条件：
# # 1.继承于type类
# # 2.定义并实现__new__，此方法要返回一个类的实例对象，因为使用元类创建类上会自动调用该方法
# class meta(type):
#     def __new__(cls,name,bases,attributes):
#         attributes['name']='initial value'
#         attributes['say']=lambda self:print('my name is',self.name)
#         return super().__new__(cls,name,bases,attributes)
# class test1(metaclass=meta):
#     pass
# print(test1.name)
# test1.name="test"
# print(test1.name)
# test1.say(test1)
# # 3.元组的使用与继承不同
# class test2(meta):
#     pass
# print(type(test1))
# print(test1)
# print(type(test2))
# print(test2)

# ****************************************************************************************

# # 多态与鸭子模型
# class WHO(object):
#     def say(self,who):
#         who.say()
# class Creature(object):
#     def say(self):
#         print("为了艾泽拉斯")
# class Trible(Creature):
#     def say(self):
#         print("为了部落")
# class League(Creature):
#     def say(self):
#         print("为了联盟")

# a=WHO()
# a.say(Creature())
# a.say(Trible())
# a.say(League())

# ****************************************************************************************

# # 枚举类
# from enum import Enum, unique
# class Gender(Enum):
#     男=1
#     女=2
#     妖=3
#     扶=4
#     伪=5
# # 可以通过多种方式调用枚举类的值
# print(Gender.男)
# print(Gender['女'])
# print(Gender(3))
# print(Gender.扶.name)
# print(Gender.伪.value)
# for gender in Gender:
#     print(gender)
# # 可以对比枚举的属性
# if not (Gender.男==Gender.伪):
#     print("真男人不是伪娘")
# # 枚举类不能对其中的属性赋值，如下是错误的
# # Gender.男=None
# @unique
# class color(Enum):
#     red=1
#     orange=2
#     yellow=3
#     green=4
#     blue=5
#     indigo=6
#     purplr=7
#     # @unique修饰符禁止枚举中出现同值属性
#     # black=7
#     # white=7
# # 也可以通过Enum直接创建一个枚举实例
# god=Enum('god',("拉","泰芙努特","舒","努特","盖布","伊西斯","欧里西斯","塞特","奈芙蒂斯"))
# for name,value in god.__members__.items():
#     print(name,"===>",value)