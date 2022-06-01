'''
有一块蛋糕重1g<=n克<=6g,已知1g、2g、3g、4g、5g、6g蛋糕分别买0,2,3,6,7,11,15元
试求解此蛋糕最贵卖多少钱
'''
"""
最优子结构

状态定义：
f(i)为切ig蛋糕售卖最高价格
p[n-i]为整块售卖(n-i)g蛋糕价格
状态转移方程：
f(n)=max{0<=i<=n|f(i)+p[n-i]}

-------------------------------------------------------

答案精进：
"""
class Solution:
    # 暴力递归
    def max_cake_price1(self,n, price_list):
        if n <= 1: return price_list[n] # 蛋糕重量 <= 1 时直接返回
        f_n=0
        if(n<=6):
            for i in range(n):  # 从 n 种组合种选择最高售价的组合作为 f(n)
                f_n = max(f_n, self.max_cake_price1(i, price_list) + price_list[n - i])
        else:
            for i in range(n-6,n):  # 从 n 种组合种选择最高售价的组合作为 f(n)
                f_n = max(f_n, self.max_cake_price1(i, price_list) + price_list[n - i])
        return f_n          # 返回 f(n)
    # 记忆化递归
    def max_cake_price2(self,n,price_list):
        if(n<=1):return price_list[n]
        memory=[0]*(n+1)
        return self.MemoRecru(n,price_list,memory)
    def MemoRecru(self,n,price_list,memory):
        if(n<=1):return price_list[n]
        if(memory[n]!=0):
            return memory[n]
        else:
            if(n<=6):
                for i in range(n):  
                    memory[n]= max(memory[n], self.MemoRecru(i, price_list,memory) + price_list[n - i])
            else:
                for i in range(n-6,n):  
                    memory[n]= max(memory[n], self.MemoRecru(i, price_list,memory) + price_list[n - i])
        return memory[n]
    # 动态规划
    def max_cake_price3(self,n, price_list):
        if n <= 1: return price_list[n] 
        dp = [0] * (n + 1)              
        for j in range(1, n + 1):       
            if(j<=6):
                for i in range(j):          
                    dp[j] = max(dp[j], dp[i] + price_list[j - i])
            else:
                for i in range(j-6,j):          
                    dp[j] = max(dp[j], dp[i] + price_list[j - i])
        return dp[n]
               
            
if __name__=="__main__":
    S=Solution()
    print(S.max_cake_price1(10, [0, 2, 3, 6, 7, 11, 15]))
    print(S.max_cake_price2(10, [0, 2, 3, 6, 7, 11, 15]))
    print(S.max_cake_price3(10, [0, 2, 3, 6, 7, 11, 15]))