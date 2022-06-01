'''
假设把某股票的价格按照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
'''
"""
最优子结构

状态定义：
dp[i]       第i天开始之后买股票的最大收益
prices[i]   第i天的股值
状态转移方程：
dp[i]=max(dp[i-1],price[i]-min(price[0:i]))
-------------------------------------------------------

答案精进：
上述方法的缺点在于price[i]-min(price[0:i])需要循环实现浪费时间与空间
答案优化在于：1.在每次循环更新当前最低股价以便直接计算最大利润。2.
状态定义：
dp[i]       第i天及之前买股票的最大收益
prices[i]   第i天的股值
cost        第i天前的最低成本
状态转移方程：
dp[i]=max(dp[i-1],price[i]-min(cost,price[i]))        

"""
class Solution:
    # 暴力递归：超时
    def maxProfit1(self, prices: list[int]) -> int:
        if(len(prices)<=1):return 0
        max_price=self.maxProfit1(prices[1:len(prices)])
        for i in range(1,len(prices)):
            if(prices[i]-prices[0]>0):
                max_price=max(max_price,prices[i]-prices[0])
        return max_price
    # 暴力递归优化1：超时
    def maxProfit2(self, prices: list[int]) -> int:
        if(len(prices)<=1):return 0
        for i in range(0,len(prices)-1):
            if(prices[i+1]>=prices[i]):
                if(i!=0):
                    return self.maxProfit2(prices[i:len(prices)])
                else:
                    break
        max_price=self.maxProfit2(prices[1:len(prices)])
        for i in range(1,len(prices)):
            if(prices[i]-prices[0]>0):
                max_price=max(max_price,prices[i]-prices[0])
        return max_price
    # 暴力递归优化2
    def maxProfit3(self, prices: list[int]) -> int:
        if(len(prices)<=1):return 0
        pos_start,pos_end=0,len(prices)-1
        for i in range(0,len(prices)-1):
            if(prices[i+1]>prices[i]):
                pos_start=i
                break
        for i in range(len(prices)-1,pos_start-1,-1):
            if(prices[i-1]<prices[i]):
                pos_end=i
                break
        if(pos_start!=0 or pos_end!=len(prices)-1):
            return self.maxProfit3(prices[pos_start:pos_end+1])
        max_price=self.maxProfit3(prices[1:len(prices)])
        for i in range(1,len(prices)):
            if(prices[i]-prices[0]>0):
                max_price=max(max_price,prices[i]-prices[0])
        return max_price
    # 答案精进
    def maxProfit(self, prices: list[int]) -> int:
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit
 
        



if __name__=="__main__":
    S=Solution()
    print(S.maxProfit3([1,2]))
