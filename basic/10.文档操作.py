# 要对文件进行操作需要导入os模块
import os
# 通过os.getcwd()获得当前路径
print(os.getcwd())
# 通过os.chdir()修改当前工作路径
os.chdir("C:\\Users\\ASUS\\Desktop\\新建文件夹")
print(os.getcwd())
# 相对路径：文件相对于当前工作目录的路径 
# 绝对路径：从根文件夹起的路径
# 在相对路径中 .\  表示当前文件夹中  ..\  表示当前文件夹的父文件夹
os.chdir("D:\\VC_Project\\python")
# 转化为绝对路径
# print(os.path.abspath(".\\"))
# 是否为绝对路径
# print(os.path.isabs("."))
# print(os.path.isabs("D:\\VC_Project\\python"))
# 从一个文件夹到另一个文件夹的路径
#但是两个文件夹需要在一个根目录下，否则将会报错
# print(os.path.relpath("D:\\VC_Project\\python","C:\\Users\\ASUS\\Desktop\\新建文件夹"))
# print(os.path.relpath("D:\\VC_Project\\python","D:\\Python_Project"))
# 当前路径最后一个分号之前的路径
# print(os.path.dirname("D:\\VC_Project\\python\\demo.py"))
# 当前路径最后一个分号之后的路径
# print(os.path.basename("D:\\VC_Project\\python\\demo.py"))
# 将当前路径分为文件夹路径与文件名（带后缀）
# print(os.path.split("D:\\VC_Project\\python\\demo.py"))
# 判断文件是否存在
# print(os.path.exists("D:\\VC_Project\\python\\demo.py"))
# 判断文件夹是否存在
# print(os.path.exists("D:\\VC_Project\\python"))
# 判断是否是文件
# print(os.path.isfile("D:\\VC_Project\\python"))
# 判断是否是文件夹
# print(os.path.isdir("D:\\VC_Project\\python"))

# **************************************************************************************************

# 文件的基本操作