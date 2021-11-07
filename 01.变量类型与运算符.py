#********
#print('''
#              稚子弄冰
#                   [宋]杨万里
#    稚子金盆脱晓冰，彩丝串取当银钲。
#    敲成玉磬传林响，忽作玻璃碎地声。
#''')
#print("""
#            四时田园杂兴
#                   [宋]范成大
#    昼出耕田夜绩麻，村庄儿女各当家。
#    童孙未解供耕织，也傍槡阴学种瓜。
#""")
#********

'''
b1=bytes('十年磨一剑',encoding="utf-8")
print("b1:",b1)
b2='磨完一剑再磨一剑'.encode('utf-8')
print("b2:",b2)
b3=b1.decode('utf-8')+','+b2.decode('utf-8')
print("b3:",b3)
'''
#**********
#在print函数中可以多输出
#name=input("Please enter your name:")
#age=input("Please enter your age:")
#print("name:",name,"age:",age)
#**********

#************
##重设print中的end参数可以改变换行设置
##shift+enter单行运行
#print('18','\t',end="")
#print('01','\t',end="")
#print('17','\t',end="")
#************


""" target=r"D:\VC_Project\python\2.txt"
print("target:",target)
f=open(target,"w")
print("为了部落",file=f)
print("为了联盟",file=f)
f.close()
print("写入成功") """



#-左对齐
#+带正负号
#0用0补齐而不是空格
#上述必须在数据长度前
#加上精度时必须有.进行分割
#+08.3精度为小数点后3位 长度为8 用0进行补齐的 带正负号的 数据

""" f=3.14159265
d=5.4445
print("%+08.3f"%f,"\n","%-08f"%d)
print("dgsfgsdfgghjryj\r") """


#
#info = "Python教程：http://c.biancheng.net/python/\n\
#C++教程：http://c.biancheng.net/cplus/\n\
#Linux教程：http://c.biancheng.net/linux_tutorial/"
#print(info)

""" print(2^4)
print(1&2)
print(2|4)
print(-9>>2)
print(~9)
print(9<<1) """

# 两次调用返回不同的对象
# 判断两个对象的内存地址，如果内存地址相同，说明两个对象使用的是同一块内存
import time  #引入time模块

""" t1 = time.gmtime() # gmtime()用来获取当前时间
t2 =  time.gmtime()
t3=t1
print(t1)
print(t2)
print(t3)
print(t1 == t2) #输出True
print(t1 is t2) #输出False
print(t1 is t3) #输出True """



url=r"http://c.biancheng.net/view/2186.html"
print("----False and xxx-----")
print( False and print(url) )
print("----True and xxx-----")
print( True and print(url) )
print("----False or xxx-----")
print( False or print(url) )
print("----True or xxx-----")
print( True or print(url) )

