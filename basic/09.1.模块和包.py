# import引入模块
import sys
print(sys.argv[0])
# import 模块名 as 别名
import sys as a
print(a.argv)
# import 模块1,模块2,模块3
import sys as a,os as b
print(a.argv)
print(b.sep)
# form 模块名 import 成员名
from sys import argv as aa,winver as bb
print(aa[0])
print(bb)
# ************************************************************************************************************
