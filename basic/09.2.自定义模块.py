'''
demo模块包括:
Person类
GENDER枚举类
'''
from enum import Enum, unique
@unique
class GENDER(Enum):
    男=1
    女=2
    无=3

# *******************************************************
class Person(object):
    def __init__(self,name,gender,age):
        if not isinstance(name,str):
            raise TypeError("name has to be str")
        else:
            self.__name=name
        if not isinstance(gender,GENDER):
            raise TypeError("name has to be GENDER")
        else:
            self.__gender=gender
        if not isinstance(age,int):
            raise TypeError("name has to be int")
        else:
            self.__age=age
    @property
    def name(self):
        ret="*"+self.__name[1,len(self.__name)-1]
        return ret
    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("name has to be str")
        self.__name=value
    @name.deleter
    def name(self):
        self.__name="***"
    @property
    def age(self):
        if(self.__gender==GENDER.男):
            return self.__age
        else:
            return "秘密"
    @age.setter
    def age(self,value):
        if not isinstance(value,int):
            raise TypeError("age has to be int")
        elif((value<0)or(value>200)):
            raise TypeError("age has to be in 0 to 200")
        else:
            self.__age=value
    @age.deleter
    def age(self):
        self.__age=0
    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self,value):
        if not isinstance(value,GENDER):
            raise TypeError("gender has to be GENDER")
        else:
            self.__gender=value
    @gender.deleter
    def gender(self):
        self.__gender=GENDER.无

    def SayHi(self):
        if(self.__gender==GENDER.男):
            g="男"
        elif(self.__gender==GENDER.女):
            g="女"
        else:
            g="未知"
        print("我是%s"%self.__name,"%s"%g,"今年%d岁"%self.__age)
# *******************************************************
print(__name__)
# 如果在当前文件中例如在demo1中print(__name__)会打印__main__
# 如果demo1作为模块输入到demo2中则在demo1中的print(__name__)会打印demo1
if(__name__=="__main__"):
    p=Person("淳.简.拉基.茨德",GENDER.男,22)
    p.SayHi()
    print(__name__)