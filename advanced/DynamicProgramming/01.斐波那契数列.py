"""
求斐波那契数列F(n)=F(n-1)+F(n-2),F(1)=1,F(0)=0
答案需要取模 1e9+7(1000000007)如计算初始结果为:1000000008,请返回 1
"""
class Solution:
    # 1.暴力递归
    def fib1(self, n: int) -> int:
        # 底层返回
        if n==0:return 0
        if n==1:return 1
        # 调用自身+顶层返回
        return (self.fib1(n-1)+self.fib1(n-2))%1000000007
    # 2.记忆化递归
    def fib2(self, n: int) -> int:
        f_array=[0]*(n+1)
        # 利用另外一个函数进行递归
        return self.fibarray(f_array,n)
    def fibarray(self,f_array:list,n:int)->int:
        # 当返回0值时直接返回0
        if n==0:return 0
        # 设置初始值，由于初始数组都是0所以F0不用在此初始化
        if n==1:f_array[1]=1
        # 当返回非零值时首先判断是否已经计算，如果计算过可直接返回值
        if f_array[n]:return f_array[n]
        # 调用自身计算斐波那契数列
        f_array[n]=(self.fibarray(f_array,n-1)+self.fibarray(f_array,n-2))%1000000007
        #顶层返回 
        return f_array[n]
    # 3.动态规划
    def fib3(self,n:int)->int:
        if n==0:return 0
        if n==1:return 1
        a,b=0,1
        for i in range(2,n+1):
            b,a=(a+b)%1000000007,b
        return b
S=Solution()
print(S.fib2(47))
print(S.fib3(47))
# print(S.fib2(6))
# print(S.fib2(7))
# print(S.fib2(8))
# print(S.fib2(9))
# print(S.fib2(10))
# print(S.fib2(11))
# print(S.fib3(43))
# print(S.fib3(44))
# print(S.fib3(45))
# print(S.fib3(8))
# print(S.fib3(9))
# print(S.fib3(10))
# print(S.fib3(11))