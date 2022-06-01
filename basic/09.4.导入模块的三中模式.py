# 使用import模块后从以下三种路径中寻找对应的模块：
# 1.当前文件所在文件夹
# 2.PYTHONPATH（环境变量）下的每个目录
# 3.python默认的安装目录
# 以上的路径都保存在sys.path中
# 如果导入的模块不在sys.path中的任何一个路径里会抛出ModuleNotFoundError异常
# 解决上述问题有以下三种方法：
# 1.向sys.path中添加模块所在路径
# 2.将模块移动到sys.path的路径中
# 3.设置path系统环境变量
import sys
print(sys.path)
sys.path.append("D:\\Python_Project")
print(sys.path)
import module
module.mod_fun()

