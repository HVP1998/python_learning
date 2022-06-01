# # __new__方法是无需staticmethod修饰的静态方法，而且会先于__init__被调用
# # 一般重写__new__方法后会需要调用super().__new__(cls)而且在返回值之前修改实例
# class demoClass:
#     instances_created = 0
#     def __new__(cls,*args,**kwargs):
#         print("__new__():",cls,args,kwargs)
#         instance = super().__new__(cls)
#         instance.number = cls.instances_created
#         cls.instances_created += 1
#         return instance
#     def __init__(self,attribute):
#         print("__init__():",self,attribute)
#         self.attribute = attribute
# test1 = demoClass("abc")
# test2 = demoClass("xyz")
# test3 = demoClass("123")
# test4 = demoClass("qwe")
# print(test1.number,test1.instances_created)
# print(test2.number,test2.instances_created)
# print(test3.number,test2.instances_created)
# print(test4.number,test2.instances_created)

# *******************************************************************************************************************************************

# # __repr__的作用是返回当前实例对象的  类名+object at+内存地址
# # print(实例对象.__repr__)相当于print(对象)
# class Planguage(object):
#     pass
# c=Planguage()
# print(c)
# print(c.__repr__())

# class PL(object):
#     def __init__(self,name,software):
#         self.__name=name
#         self.__software=software
#     def __repr__(self):
#         print("PL"+"name:",self.__name+"\t"+"software:",self.__software)
    
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         if not isinstance(value,str):
#             raise TypeError("name has to be str")
#         self.__name=value
#     @name.deleter
#     def name(self):
#         self.__name="NONE"
#     @property
#     def software(self):
#         return self.__software
#     @software.setter
#     def software(self,value):
#         if not isinstance(value,str):
#             raise TypeError("software has to be str")
#         self.__software=value
#     @software.deleter
#     def software(self):
#         self.__software="NONE"

# C=PL("C","Code::Blocks")
# python=PL("python","IDLE(python3.9)")
# Java=PL("Java","IDEA")
# C_add=PL("C++","visual C++ 6.0")
# Csharp=PL("C#","Visual Studio 2019")
# print(C.__repr__())
# print(python.__repr__())
# print(Java.__repr__())
# print(C_add.__repr__())
# print(Csharp.__repr__())

# *******************************************************************************************************************************************

# # __del__
# # python有自动的垃圾回收机制，当一个实例对象不再被使用则利用自动销毁机制调用__del__对其占用的资源进行回收
# # python采用自动引用技术（ACR）对垃圾进行回收，当有一个实例创建的时候对应对象的计数加1，当有一个实例调用__del__的时候计数减1如果计数器为0则进行垃圾回收
# # 如果有子类对父类的__del__进行重写如果需要对子类实例对象回收资源时需要显式调用父类的__del__才能保证资源的全部释放

# class PL:
#     def __init__(self):
#         print("调用父类__init__()创建实例对象")
#     def __del__(self):
#         print("调用父类__del__()实现垃圾回收")
# class python(PL):
#     def __init__(self):
#         print("调用子类__init__()创建实例对象")
#     def __del__(self):
#         print("调用子类__del__()对垃圾回收")
# # 创建实例对象计数加一C=1
# p=PL()
# # 引用实例对象计数加一C=2
# l=p
# # 调用del计数减一C=1
# del p
# print("************")
# # 调用del计数减一C=0
# del l
# print("------------")
# python3=python()
# PL.__del__(python3)

# *******************************************************************************************************************************************

# # dir() 函数的内部实现，其实是在调用参数对象 __dir__() 方法的基础上，对该方法返回的属性名和方法名做了排序。
# # 该方法还会返回父类中的方法
# class Person(object):
#     def __init__(self):
#         pass
#     def SayHello(self):
#         pass
# p=Person()
# print(dir(p))
# print(p.__dir__())

# *******************************************************************************************************************************************

# # __dict__
# class bird(object):
#     def __init__(self,name):
#         self.__name=name
#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self,value):
#         if not isinstance(value,str):
#             raise TypeError("name has to be str")
#         self.__name=value
#     @name.deleter
#     def name(self):
#         self.__name="***"
#     def wing(self):
#         print("has wings")
#     def fly(self):
#         print("can fly")

# class ostrich(bird):
#     def character(self):
#         print("can run fastly")

# o=ostrich("鸵鸟")
# o.runfast=True
# b=bird("鸟")
# # 对象会返回实例方法与实例属性
# print(b.__dict__)
# print(o.__dict__)
# # 类会返回所有除实例成员外的成员
# print(bird.__dict__)
# print(ostrich.__dict__)
# # 可以利用__dict__改变对应的成员
# o.__dict__['runfast']="40km/h"
# print(o.runfast)

# *******************************************************************************************************************************************

# # hasattr  getattr  setattr  issubclass  isinstance
# # hasattr(对象名,"属性或方法名")    属性或方法是否存在于此类名中
# # getattr(对象名,"属性或方法名","默认值")    获取类中的属性或方法，如果不存在则返回默认值
# # setattr(对象名,"属性或方法名"，参数)  将参数付给属性或方法，如果不存在则创建此属性或方法
# from enum import Enum
# GEMDER=Enum('GENDER',("男","女"))
# class person(object):
#     sayhello="hello"
#     def __init__(self,name,gender,age):
#         self.__name=name
#         self.__gender=gender
#         self.__age=age
#     @property
#     def name(self):
#         return self.__name
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
#         return self.__gender.name
#     @gender.setter
#     def gender(self,value):
#         if not isinstance(value,GEMDER):
#             raise TypeError("name has to be GENDER")
#         self.__gender=value
#     @gender.deleter
#     def gender(self):
#         self.__gender=None
#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self,value):
#         if not isinstance(value,int):
#             raise TypeError("name has to be int")
#         self.__age=value
#     @age.deleter
#     def age(self):
#         self.__age=0
# class student(person):
#     pass
# p=person("张三",GEMDER.男,18)
# print(hasattr(p,"name"))
# print(hasattr(p,"sayhello"))
# print(getattr(p,"sayhello"))
# print(getattr(p,"say","nosay"))
# def say(self):
#     print("hello")
# setattr(p,"sayhello",12)
# print(getattr(p,"sayhello"))
# setattr(p,"sayhello",say)
# p.sayhello(p)
# s=student("李蕾",GEMDER.女,16)
# print(isinstance(s,(person,object)))
# print(issubclass(s,(person,object)))

# *******************************************************************************************************************************************

# # __call__
# # 可调用对象：可以将()直接运用于自身并执行的都称为可调用对象，例如函数
# # "函数()"其实相当于"函数.__call__()"
# # 在类中重写__call__可以将类变成可调用对象
# class PL(object):
#     def __init__(self,name,software):
#         self.name=name
#         self.software=software
#     def __call__(self):
#         print("THE CODE:",self.name)
#         print("THE SOFTWARE:",self.software)
#     def say(self):
#         print("你看你🐎 呢?")
# p=PL("python","Visual Studio Code")
# p()
# if(hasattr(p,"name")):
#     print("是否是函数",hasattr(p.name,"__call__"))
# if(hasattr(p,"say")):
#     print("是否是函数",hasattr(p.say,"__call__"))

# *******************************************************************************************************************************************

# # 在类中可以对运算符进行重载
# # 所谓运算符重载就是在类中定义一个与运算符对应的处理方法，这样在类对象在进行运算符操作时，系统就会调用类中相应的处理方法来处理
# class Student(object):
#     def __init__(self,name,ID,score):
#         self.name=name
#         self.ID=ID
#         self.score=score
#     def __str__(self):
#         return "名字："+self.name+"\t"+"学号："+self.ID+"\t"+"成绩："+self.score
#     __repr__=__str__   #转化为供解释器读取的形式
#     def __lt__(self,record):
#         score1=float(self.score)        
#         score2=float(record.score)
#         print(score1)
#         print(score2)
#         if(score1<score2):
#             return True
#         else:
#             return False
#     def __gt__(self,record):
#         score1=float(self.score)
#         score2=float(record.score)
#         if(score1>score2):
#             return True
#         else:
#             return False
#     def __add__(self,record):
#         score1=float(self.score)
#         score2=float(record.score)
#         return (score1+score2)/2
# s1=Student("李雷","1662510210","4.7")
# s2=Student("韩梅梅","1662510211","5")
# print(str(s1))
# print(repr(s2))
# print(s2)
# print(s2<s1)
# print(s2>s1)
# print(s1+s2)

# *******************************************************************************************************************************************

# # # 利用__iter__和__next__可以将类改写为迭代器
# # # 1.可迭代对象不一定是迭代器
# # # 2.迭代器一定是可迭代对象
# # # 3.容器类型(str、lsit、dict、set、tuple)是可迭代对象但是不是迭代器
# # from collections import Iterable
# # from collections import Iterator
# # import time

# # class Person(object):
# #     def __init__(self):
# #         self.List_name=list()
# #         self.List_num=0
# #     def add(self,arg):
# #         self.List_name.append(arg)
# #     def ext(self,arg):
# #         self.List_name.extend(arg)
# #     def __iter__(self):
# #         return self
# #     def __next__(self):
# #         if self.List_num<len(self.List_name):
# #             ret=self.List_name[self.List_num]
# #             self.List_num+=1
# #             return ret
# #         else:
# #             raise StopIteration
# #     def __setitem__(self,key,value):
# #         self.List_name.insert(key,value)

# # p=Person()
# # p.add("拉")
# # p.add("舒")
# # p.add("泰芙努特")
# # p.add("盖布")
# # p.add("努特")
# # p.add("欧里西斯")
# # p.add("伊西斯")
# # p.add("塞特")
# # p.add("伊西斯")
# # print("是否时可迭代对象：",isinstance(p,Iterable))
# # print("是否是迭代器：",isinstance(p,Iterator))
# # p[10]="布拉"
# # for name in p:
# #     print(name)
# #     time.sleep(0.5)
# # 迭代器是一个可以记住遍历位置的对象，因此不会像列表那样一次性全部生成，而是可以等到用的时候才生成，因此节省了大量的内存资源
# # 迭代器的优势在于不会创建一个列表从已知数据中读取，而是在需要的时候生成相关数据。
# # 应用生成斐波那契数列（后一项是前两项数据的和）
# import time
# class Fibonacci(object):
    
#     def __init__(self,num):
#         self.Fib_num=num
#         self.i=0
#         self.a=0
#         self.b=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         ret=self.a
#         if(self.i<self.Fib_num):
#             self.a,self.b=self.b,self.a+self.b
#             self.i+=1
#         else:
#             raise StopIteration
#         return ret
# f=Fibonacci(6)
# for num in f:
#     print(num)
#     time.sleep(1)

# *******************************************************************************************************************************************

# # 利用迭代器逆向输出字符串
# class Reverse: 
#     def __init__(self, string): 
#         self.__string = string 
#         self.__index = len(string) 
#     def __iter__(self):
#         return self 
#     def __next__(self): 
#         if self.__index == 0: 
#             raise(StopIteration)     
#         self.__index-=1 
#         return self.__string[self.__index] 
# revstr = Reverse('Python') 
# for c in revstr: 
#     print(c,end=" ")

# *******************************************************************************************************************************************

# # 生成器
# # 1.创建生成器的条件：①存在一个以yield为返回值关键字的函数②调用函数即可创建生成器
# # 2.生成器关键字yield执行完以后会暂停当前的程序
# # 3.可以利用next函数继续进行
# # 4.next函数和for都是在底层实现了__next__函数
# # 5.也可以利用list和tuple来直接将生成器能生成的所有值存储成列表或者元组的形式
# # 6.lsit和tuple的底层实现和for相似

# import time
# def NUM(num):
#     print("START")
#     for i in range(1,num+1):
#         yield i
#         print("CONTINUE")
#     return "DONE"
# # n1=NUM(6)
# # for i in n1:
# #     print(i)
# #     time.sleep(1)
# # n2=NUM(7)
# # for i in range(0,7):
# #     print(next(n2))
# # n3=NUM(8)
# # for i in range(0,8):
# #     print(n3.__next__())
# # n4=NUM(9)
# # print(list(n4))
# # n5=NUM(4)
# # print(tuple(n5))
# # n6=NUM(3)
# # print(set(n6))
# n7=NUM(10)
# while(True):
#     try:
#         x=next(n7)
#         print(x)
#     except StopIteration as e:
#         print("是否完成遍历：%s"%e.value)
#         break

# *******************************************************************************************************************************************

# # 生成器也是一种迭代器
# from collections.abc import Iterator
# from collections.abc import Generator
# def fib(num):
#     a,b=0,1
#     i=0
#     while(True):
#         if(i<num):
#             a,b=b,a+b
#             i+=1
#             yield a
#         else:
#             break
#     return "Iteration Done"
# f=fib(3)
# # 1.可以利用isinstance判断
# print(isinstance(f,Iterator))
# # 2.可以利用issubcalss判断
# print(issubclass(Generator,Iterator))
# # 3.可以利用id来判断
# print(id(f))
# print(id(iter(f)))
# # 4.可以利用dir来看生成器里是否有__iter__与__next__
# print(dir(f))
# print(f.__dir__())
# # 5.可以利用__bases__来看生成器的父类是谁
# print(Generator.__bases__)
# # 6.可以利用__mro__来看生成器的继承树
# print(Generator.__mro__)
# 7.取两个集合的差集
# set(dir(Generator)) - set(dir(Iterator))

# *******************************************************************************************************************************************

# # send  给函数传值
# def func1():  
#     print("ok1")
#     x = 10  
#     print(x)
#     x = yield 1  
#     print(x)
#     yield x 
# # 得到生成器对象f1 
# f1 = func1()  
# # 起动生成器（也叫激活生成器、预激生成器）
# # 传递的值必须为None，否则报错
# # ret1 = f1.send(None)
# # next也是起动生成器的一种方式 
# ret1 = next(f1)
# print(ret1)
# ret2 = f1.send('eee')
# print(ret2)
# # import sys
# # def SendValue():
# #     x=10
# #     y=-1
# #     print("x：%d"%x,"y：%d"%y)
# #     x=yield 1
# #     print("x：",x)
# #     y=yield 2
# #     print("y：",y)

# # s=SendValue()
# # # ret=next(s)


# ret=s.send(None)
# print("第一次yeild返回的值：",ret)
# ret=s.send("send")
# print("第二次yeild返回的值：",ret)
# try:
#     ret=s.send("test")
# except StopIteration:
#     exc_type, exc_value, exc_tb = sys.exc_info()
#     print('异常类型：%s' % exc_type)
#     print('异常值：%s' % exc_value)
#     print('异常追踪信息：%s' % exc_tb)


# *******************************************************************************************************************************************

# # throw
# # 在生成器暂停的地方抛出类型为 type 的异常，并返回下一个 yield 的返回值。
# def gen1():
#     n = 0
#     while True:
#         try:
#             yield n
#             n += 1
#         except ZeroDivisionError:
#             print('捕获到了 ZeroDivisionError')
#             print('此时的 n 为：%s' % n)
# # 创建一个生成器对象
# g = gen1()
# # 激活生成器，并利用yield返回值给ret
# ret = next(g)
# # ret=0
# print('第一次 yield 的返回值：%s' % ret)
# print()
# # 此时程序怎停在yield返回值以后，抛出异常（中间跳过了n+=1）并通过yield返回下一个值
# ret = g.throw(ZeroDivisionError)
# # 因为跳过了n+=1所以n=0, ret=0
# print('第二次 yield 的返回值：%s' % ret)
# print()
# # 此时会运行n+=1所以返回1，ret=1
# ret = next(g)
# print('第三次 yield 的返回值：%s' % ret)
# print("*******************************************************")

# # 如果生成器函数没有捕获并处理传入的异常，或者说抛出了另一个异常，那么该异常会被传递给调用方。
# import sys
# def gen2():
#     n=0
#     while True:
#         yield n
#         n+=1
# g=gen2()
# ret1=next(g)
# # 在生成器中没有处理对应异常将会返回给调用方
# try:
#     ret2=g.throw(ZeroDivisionError)
# except ZeroDivisionError:
#     print("捕获ZeroDivisionError错误")
#     print(sys.exc_info)
# # 由于没有通过throw返回值，ret2不存在
# try:
#     print(ret2)
# except NameError:
#     print("捕获NameError错误")
#     print(sys.exc_info)
# # 对于已经通过抛出异常而退出的生成器再使用 next(g) 会持续抛出 StopIteration 异常
# try:
#     ret3=next(g)
# except StopIteration:
#     print("捕获StopIteration错误")
#     print(sys.exc_info)     
# print("*******************************************************")

# # 如果生成器退出时还没有 yield 新值，则会抛出 StopIteration 异常
# def gen3():
#     try:
#         yield 1
#     except Exception as e:
#         print('在生成器内部捕获了异常')
#         print(e.args)
#         print('处理完毕，假装什么也没发生')
#         print()
# g=gen3()
# ret=next(g)
# try:
#     ret=g.throw(TypeError,"错误类型")
# except StopIteration:
#     print("捕获StopIteration")
#     print(sys.exc_info)

# *******************************************************************************************************************************************

# # close
# # 没有对异常处理的生成器，不捕获GeneratorExit异常，close返回调用方法，不传递异常
# print("----1----")
# def gen1():
#     print("返回值：1")
#     yield 1
#     print("返回值：2")
# g1=gen1()
# ret1=next(g1)
# print(ret1)
# g1.close()
# try:
#     g1.__next__()
# except StopIteration:
#     print("捕获到stopiteration异常")
# print("******************************************************")
# # 正常的生成器结束调用，不会返回异常
# print("----2----")
# def gen2():
#     try:
#         yield 1
#     except GeneratorExit:
#         print("正常返回generatorexit异常")
#     print("生成器函数结束了")
# g2=gen2()
# ret2=g2.__next__()
# print(ret2)
# g2.close()
# print("******************************************************")
# # 在generatorexit之后还有yield语句则会返回runtimeerror，在
# print("----3----")
# def gen3():
#     try:
#         yield 1
#     except GeneratorExit:
#         print("捕获到GeneratorExit异常")
#         print("现在尝试在GeneratorExit之后使用yield返回值")
#         yield 2
# g3=gen3()
# ret3=next(g3)
# print(ret3)
# try:
#     g3.close()
# except RuntimeError:
#     print("捕获到RuntimeError异常")
# print("******************************************************")
# # 可以利用bool变量
# # finally语句与try语一起使用在结束try模块时一定会运行finally语句
# print("----3.5----")
# def safegen():
#     yield 'so far so good'
#     closed = False
#     try:
#         yield 'yay'
#     except GeneratorExit:
#         closed = True
#         raise
#     finally:
#         if not closed:
#             yield 'boo'
# print("******************************************************")
# # 对于已经关闭的生成器close不会有任何操作
# print("----4----")
# def gen4():
#     try:
#         yield 1
#     except GeneratorExit:
#         print("捕获GeneratorExit异常")
# g4=gen4()
# ret=g4.__next__()
# print(ret)
# g4.close()
# g4.close()
# g4.close()
# print("******************************************************")

# *******************************************************************************************************************************************

# # @函数装饰器
# # 被装束函数无传入参数
# # 被装饰函数相当于装饰函数的形参
# def Afunc(f):
#     print("函数Afunc开始")
#     f()
#     print("函数Afunc结束")
#     return "我是被修饰的函数"
# @Afunc
# def Bfunc():
#     print("函数Bfunc开始")
#     print("函数Bfunc结束")
# # 被修饰的函数不同于其他的函数
# # 如果修饰函数（Afunc），返回的是一个值则被修饰函数（Bfunc）就是一个普通变量
# # 如果修饰函数（Afunc），返回的是一个函数则被修饰函数（Bfunc）就是一个函数
# print(Bfunc)
# print("******************************************************")
# 被装饰函数有传入参数
# 需要在装饰函数中创建一个与被装饰函数具有相同形参的函数
# import time
# def Cfunc(func):
#     def temp(a,b):
#         starttime=time.time()
#         func(a,b)
#         endtime=time.time()
#         t=(endtime-starttime)*1000
#         print("this func spend %sms"%t)
#     return temp
# @Cfunc
# def Dfunc(a,b):
#     print("this func is to add two numbers")
#     time.sleep(1)
#     print("the result=%d"%(a+b))
# if __name__=="__main__":
#     D=Dfunc(5,6)
# print("******************************************************")
# # 被装饰函数有多传入参数
# # 需要用到多参数传递
# def Efunc(func):
#     def temp(*args,**argss):
#         starttime=time.time()
#         func(*args,**argss)
#         endtime=time.time()
#         t=(endtime-starttime)*1000
#         print("this func spends %sms"%t)
#     return temp
# @Efunc
# def Ffunc(a,b,c):
#     print("this func is to add numbers")
#     time.sleep(1)
#     print("the result=%s"%(a+b+c))
# @Efunc
# def Gfunc(a,b,c,d):
#     print("this func is to add numbers")
#     time.sleep(1)
#     print("the result=%s"%(a+b+c+d))
# f=Ffunc(1,2,3)
# f=Gfunc(5,6,7,8)
# print("******************************************************")
# # 一个函数也可以被多个装饰器装饰
# def Hfunc(func):
#     print("这是第一个装饰器")
#     def temp(a,b):
#         starttime=time.time()
#         func(a,b)
#         endtime=time.time()
#         t=(endtime-starttime)*1000
#         print("this func spends %sms"%t)
#     return temp
# def Ifunc(func):
#     print("这是第二个装饰器")
#     def temp(a,b):
#         starttime=time.time()
#         func(a,b)
#         endtime=time.time()
#         print("startime is %s"%starttime,"and endtime is %s"%endtime)
#     return temp
# @Ifunc
# @Hfunc
# def Jfunc(a,b):
#     print("这是一个求和函数")
#     time.sleep(1)
#     print("结果是%s"%(a+b))
# j=Jfunc(1,2)
# print("******************************************************")
# 多个修饰器下的运行顺序是从下向上
# 如下test()=dec1(dec2(test))
# 1.dec2(test)返回two
# 2.def1(two)返回one
def dec1(func):  
    print("1111")  
    def one():  
        print("2222")  
        func()  
        print("3333")  
    return one  
  
def dec2(func):  
    print("aaaa")  
    def two():  
        print("bbbb")  
        func()  
        print("cccc")  
    return two  
 
@dec1  
@dec2  
def test():  
    print("test test")  
  
test()  

























    