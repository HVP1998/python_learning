# # 关键字参数
# # 函数中可以利用：表示虚拟参数的类型，用->表示函数返回值的类型
# def PrintStr(str1:str,str2:str)->str:
#     print("str1:",str1,"\t",end="")
#     print("str2:",str2)
# # SyntaxError: positional argument follows keyword argument
# # PrintStr(str1="123","456")
# # Get mutiple values for argument str1
# # PrintStr("123",str1="456")
# PrintStr("123",str2="456")
# PrintStr(str1="abc",str2="def")


# # 默认参数
# # SyntaxError: non-default argument follows default argument
# # def PrintStr(str1="123",str2):
# #     print("str1:",str1,"\t",end="")
# #     print("str2",str2)
# def PrintStr(str1,str2="456"):
#     print("str1:",str1,"\t",end="")
#     print("str2",str2)
# PrintStr("456","789")


# # 多参数传递
# # 传入参数中如果有字典字典的key必须是字符串
# def PrintStr(*str1,**str2):
#     s=""
#     for i in str1:
#         s=s+str(i)
#     print("str1:",s)
#     s=""
#     for i in str2:
#         s=s+str2[i]
#     print("str2:",s)
#     # for item in str1:
#     #     print(type(item))
#     # for item in str2:
#     #     print(type(str2[item]))
# dic={"1":"1","2":"2","3":"3"}
# tup="a","b","c"
# # 注意在实际参数前加上修饰符
# PrintStr(*tup,**dic)
# l=[3.14,159,265]
# PrintStr(*l,**dic)


# # 逆向参数收集
# def GetMax(num1,num2):
#     print("max num:",num1 if num1>num2 else num2)
# # 对元组解包
# tup=(3.14,3.145)
# GetMax(*tup)
# # 对列表解包
# l=[2.5,2.75]
# GetMax(*l)
# # 对集合解包
# s={2e-2,3E-5}
# GetMax(*s)
# # 在字典的解包中必须将字典的键与函数的形式参数一一对应
# dic={'num1': 5+1, 'num2': 12+5}
# GetMax(**dic)


# # 无返回参数的函数会默认返回None
# def ADD_10(num1):
#     num1+=10
# arg=ADD_10(20)
# print(arg)
# str1=""
# str2=[]
# print(arg is str1)
# print(arg is str2)


# # 偏函数
# from functools import partial
# # 使用partial
# import functools
# # 使用functools.partial
# def mod(m,key=2):  
#  return m % key == 0  
# mod_to_2 = partial(mod,key=2)  
# print('A__3___使用原函数的默认关键字参数对2进行求余：')  
# print(mod(3))                           #对2进行求余-- 原函数 使用默认参数  
# print('B__3___使用偏函数对2进行求余：')  
# print(mod_to_2(3))                      #对2进行求余-- 新函数 --偏函数产生  
# mod_to_5 = functools.partial(mod,key=5)   
# print('C__25___使用原函数的关键字参数对5进行求余：')  
# print(mod(25,key=5))                    #对5进行求余 -- 原函数  
# print('D__25___使用偏函数对5进行求余：')  
# print(mod_to_5(25))                     #对5进行求余 -- 新函数--偏函数产生 


# # 作用域
# def PrintStr(str1,str2):
#     str3="with time going by"
#     print(str1)
#     print(str2)
#     print("locals：",locals()['str3'])
# str1="no time to die"
# str2="this is chance"
# PrintStr(str1,str2)
# print("globals：",globals()['str1'])
# print("globals：",globals()['str2'])
# globals()['str1']="James Bond"
# print(globals()['str1'])


# #将函数赋值给变量
# def GetSum(num1,num2):
#     return num1+num2
# def GetMutiple(num1,num2):
#     return num1*num2
# Result=GetSum
# print(Result(10,20))
# Result=GetMutiple
# print(Result(3,10))
# #将函数作为实参传入函数
# def GetResult(num1,num2,fun):
#     return fun(num1,num2)
# print(GetResult(5,6,GetMutiple))
# print(GetResult(15,15,GetSum))
# #在函数内部的函数称为局部函数如果作为值返回则可在函数外调用局部函数
# def A_Function():
#     def Local_Function():
#         print("Local Function go out the circule")
#     return Local_Function
# out_func=A_Function()
# out_func()


#局部函数中与函数中同名的变量将会覆盖原有变量
def outdef ():
    name = "所在函数中定义的 name 变量"
    #局部函数
    def indef():
        nonlocal name
        print(name)
        #修改name变量的值
        name = "局部函数中定义的 name 变量"
    indef()
    print(name)
#调用全局函数
outdef()

# #闭包函数，其中 exponent 称为自由变量
# def nth_power(exponent):
#     def exponent_of(base):
#         return base ** exponent
#     return exponent_of # 返回值是 exponent_of 函数
# square = nth_power(2) # 计算一个数的平方
# cube = nth_power(3) # 计算一个数的立方

# print(square(2))  # 计算 2 的平方
# print(cube(2)) # 计算 2 的立方


# # lambda表达式（匿名函数）
# def GetSun(num1,num2):
#     return num1+num2
# print(GetSun(1,2))
# Get_lambda_Sum=lambda x,y:x+y
# print(Get_lambda_Sum(3,4))


# # exec()只执行其中的语句不返回值
# # eval()执行后返回其中的值
# a=1E5
# exec("a=a+2E4")
# print("exec执行a=a+2E4,a=",a)
# a=exec("a+2E4")
# print("执行a=exec(\"a+2E4\"),a=",a)
# b=10
# b=eval("b+20")
# print("执行b=eval(\"b+20\"),b=",b)

# def GetName(name):
#     return name.upper()[0]+name.lower()[1:len(name)]
# while(True):
#     b=True
#     n=input("输入一个英文名：")
#     for i in n:
#         if((i>='a')and(i<='z'))or((i>='A')and(i<='Z')):
#             pass
#         else:
#             b=False
#             print("英文名只能由字母组成")
#             break
#     if(b):
#         print("是个正常的英文名！")
#         break
#     else:
#         continue

# # map(arg1,arg2)函数
# # arg1是一个函数
# # arg2是一个序列
# # 返回一个map可以转换成列表
# def fun1(x):
#     return x*x
# l1=range(1,11)
# l1=list(map(fun1,l1))
# print(l1)


# # reduce(arg1,arg2)函数
# # arg1是一个函数
# # arg2是一个序列
# # 返回一个数值
# from functools import reduce
# def fun2(x,y):
#     return x+y
# l2=range(1,11)
# l2=reduce(fun2,l2)
# print(l2)


# # filter(arg1,arg2)函数
# # arg1是一个函数
# # arg2是一个序列
# # 根据返回True还是False删除序列中的元素
# def fun3(x):
#     return x%2==1
# l3=range(0,11)
# l3=list(filter(fun3,l3))
# print(l3)


# # sorted(arg1,key=arg2)函数
# # arg1是一个序列
# # arg2是一个关键字可省略
# # 根据arg2对arg1进行排序
# l4=[12,1E2,1.2,-2E3,7/2]
# l4=sorted(l4,key=abs)
# print(l4)