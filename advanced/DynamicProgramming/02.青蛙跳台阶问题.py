'''
一只青蛙一次可以跳上1级台阶,也可以跳上2级台阶。求该青蛙跳上一个n级的台阶总共有多少种跳法。
答案需要取模 1e9+7(1000000007),如计算初始结果为:1000000008,请返回 1。
'''

"""
重叠子问题

状态定义：

状态转移方程：

-------------------------------------------------------

答案精进：
"""
class Solution:
    # 1.暴力递归
    def numWays1(self, n: int) -> int:
        # 底层返回：由于只剩一阶台阶的情况只有一种上法（最后上一级台阶）等同于只剩零阶台阶（完成上台阶）都属于最后的底层返回
        if n==0 or n==1:return 1
        # 调用自身+顶层返回
        return (self.numWays1(n-1)+self.numWays1(n-2))%1000000007
    # 2.记忆化递归
    def numWays2(self,n:int)->int:
        numway_li=[0]*(n+1)
        return self.numWayArray(n,numway_li)
    def numWayArray(self,n:int,num_li:list)->int:
        if n==0 or n==1:return 1
        if num_li[n]:return num_li[n]
        num_li[n]=(self.numWayArray(n-1,num_li)+self.numWayArray(n-2,num_li))%1000000007
        return num_li[n]
    # 3.动态规划
    def numWays3(self,n:int)->int:
        if n==0 or n==1:return 1
        a,b=1,1
        for i in range(2,n+1):
            b,a=(a+b)%1000000007,b
        return b
S=Solution()
# print(S.numWays1(30))
print(S.numWays2(500))
print(S.numWays3(500))
    