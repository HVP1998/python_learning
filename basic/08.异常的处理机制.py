# # 异常捕获和异常处理
# # 1.执行try中的代码如果出现异常则系统生成一个异常类型并提交给python解释器（异常捕获）
# # 2.寻找异常对应的except块
# # 3.找到对应的except块：将异常对象交给python处理（异常处理）
# #   没有对应的except块：程序终止运行，python解释器退出
# try:
#     assert(1==1.01)
# except AssertionError:
#     print("1不等于1.01")
# # 一个try模块中可以包含多个except
# # 一个except也可以包含多个异常类型
# # Except表示所有的异常类型，可以放在最后一个except语句中
# # 在except后面不写任何参数与Except是一样的
# try:
#     a=int(input("输入除数："))
#     b=int(input("输入被除数："))
#     c=b/a
#     print(c)
# except(ArithmeticError,ValueError):
#     print("各种算术错误引发的异常",end="")
#     print("，或者操作或者函数收到正确的类型但是不合适的参数")
# except(SystemError):
#     print("解释器内部发现错误")
# except Exception:
#     print("其他未知错误")
# # except:
# #     print("其他未知错误")

# *******************************************************************************************************************************************

# # try...except...except...else...
# # 如果try捕获到异常则调用相应的except处理异常，若没有出现异常则调用else后的语句
# try:
#     result=30/int(input("请输入除数："))
#     print("输出答案：%+010.5f"%result)
# except ArithmeticError:
#     print("算术错误")
# except ValueError:
#     print("输入数据错误必须为常数")
# except:
#     print("其他未知错误")
# else:
#     print("没有出现错误")
# print("程序结束")

# *******************************************************************************************************************************************

# # finally无论try中的语句是否有异常都会运行
# try:
#     result=20/int(input("请输入除数："))
#     print("输出答案：%+010.5f"%result)
# except ArithmeticError:
#     print("算术错误")
# except ValueError:
#     print("输入数据错误必须为常数")
# except:
#     print("其他未知错误")
# else:
#     print("没有出现错误")
# finally:
#     print("程序结束")

# *******************************************************************************************************************************************

# # raise手动抛出异常
# # raise在没有参数的时候会默认抛出runtime异常
# try:
#     a = input("输入一个数：")
#     # isdigit   所有的字符是数字
#     # isalpha   所有的字符是字母
#     # islower   所有的字符是小写
#     # isupper   所有的字符是大写
#     # istitle   所有的字符是首字母大写
#     # isspace   所有的字符是空白字符\t \n \r 
#     if(not a.isdigit()):
#         raise
# except RuntimeError as e:
#     print("引发异常：",repr(e))

# *******************************************************************************************************************************************

# # 利用sys中的exc_info方法可以获得详细的异常信息
# import sys
# try:
#     result=20/int(input("请输入除数："))
#     print("输出答案：%+010.5f"%result)
# except ArithmeticError:
#     print("算术错误")
#     print(sys.exc_info())
# except ValueError as e:
#     print("输入数据错误必须为常数")
#     print(e.__repr__())
#     print(e.args)
# except:
#     print("其他未知错误")
#     print(sys.exc_info())
# else:
#     print("没有出现错误")
# finally:
#     print("程序结束")

# *******************************************************************************************************************************************

# # traceback
# # traceback.print_exc(exc._etype,exc_value,exc_tb,file)
# import traceback

# class SelfException(Exception):
#     pass
# def fun1():
#     fun2()
# def fun2():
#     fun3()
# def fun3():
#     fun4()
# def fun4():
#     raise SelfException("自定义异常")
# try:
#     fun1()
# except:
#     traceback.print_exc()
#     traceback.print_exc(file=open("run.txt","a"))

# *******************************************************************************************************************************************

# 自定义异常类
class MoneyException(Exception):
    '''自定义的异常类'''
 
    def __init__(self, money):
        self.money = int(money)
 
    def __str__(self):
        if self.money > 0:
            return "Good!"
        else:
            return "Gun!"
 
 
try:
    money = -100
    if money > 0:
        exc = MoneyException(money)
        print(exc)
    else:
        raise MoneyException(money)
except MoneyException as e:
    print("自己留着吧!", e)