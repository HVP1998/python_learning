'''
我们把只包含质因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数。
'''

"""
状态定义：
dp[i]   i为丑数
转移方程：
dp[i]=True  i为丑数
dp[i]=False i不为丑数

-------------------------------------------------------

答案精进：
此方法在原有丑数基础上乘丑数因子不需要逐个判断数字是否为丑数所以比较迅速
状态定义：
dp[i]   第i个丑数
a       丑数因子2要乘的数字
b       丑数因子3要乘的数字
c       丑数因子5要乘的数字
状态转移方程：
dp[i]=min(dp[a]*2,dp[b]*2,dp[c]*2)

"""
class Solution:
    # 循环
    def nthUglyNumber1(self, n: int) -> int:
        if(n<=6):return n
        n=n-6
        tmp=6
        while(n>=1):
            tmp+=1
            num=int(tmp)
            while(num!=1):
                if(num%5==0):num/=5
                elif(num%3==0):num/=3
                elif(num%2==0):num/=2
                else:break
            if(num==1):n-=1
        return tmp
    # 循环+字典
    def nthUglyNumber2(self, n: int) -> int:
        if(n<=6):return n
        dic=dict()
        for i in range(1,7):
            dic[i]=True
        n=n-6
        tmp=6
        while(n>=1):
            tmp+=1
            num=int(tmp)
            while(num!=1):
                if(dic.get(num)==True):num=1
                elif(dic.get(num)==False):break
                if(num%5==0):num/=5
                elif(num%3==0):num/=3
                elif(num%2==0):num/=2
                else:break
            if(num==1):
                n-=1
                dic[tmp]=True
            else:
                dic[tmp]=False
        return tmp
    # 答案：
    def nthUglyNumber3(self, n: int) -> int:
        dp, a, b, c = [1] * n, 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2: a += 1
            if dp[i] == n3: b += 1
            if dp[i] == n5: c += 1
        return dp[-1]



if __name__=="__main__":
    S=Solution()
    print(S.nthUglyNumber2(500))
    # print(S.nthUglyNumber3(800))