'''
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
'''
"""
定义状态：
dp[i]当前数字，dp[i-1]将最后一个数字作为字符，dp[i-2]将最后两个数字作为字符
状态转移方程：
dp[i]=dp[i-1]+dp[i-2]，num%100<=25 and num%100-num%10!=0
dp[i]=dp[i-1]        ，num%100>25 or (num%100<=25 and num%100-num%10==0)
其中num%100-num%10!=0主要是消去“01”、“02”这种前加0的不可翻译字符

答案精进：
dp[i]=dp[i-1]+dp[i-2]，10<=num%100<=25
dp[i]=dp[i-1]        ，num%100>25 or num%100>10
10<=num%100<=25同时除去大于25和为01、02等前加0无法转化的情况

除了一下展示的“整数取余方案”也有“整数转字符串方案”思路类似在此不表
""" 


class Solution:
    # 暴力递归
    def translateNum1(self, num: int) -> int:
        if(num<=9):return 1
        if(num%100<=25 and num%100-num%10!=0):
            return self.translateNum1(int((num-num%10)/10))+self.translateNum1(int((num-num%100)/100))
        else:
            return self.translateNum1(int((num-num%10)/10))
    # 记忆化递归
    def translateNum2(self, num: int) -> int:
        if(num<=9):return 1
        count,tmp=0,num
        while(tmp!=0):
            count+=1
            tmp=int(tmp/10)
        memory=[0]*count
        return self.MemoRecru(num,count,memory)
    def MemoRecru(self,num:int,count:int,memory:list):
        if(num<=9):return 1
        if(memory[count-1]!=0):return memory[count-1]
        if(num%100<=25 and num%100-num%10!=0):
            memory[count-1]=self.MemoRecru(int((num-num%10)/10),count-1,memory)+self.MemoRecru(int((num-num%100)/100),count-2,memory)
        else:
            memory[count-1]=self.MemoRecru(int((num-num%10)/10),count-1,memory)
        return memory[count-1]
    # 动态规划
    def translateNum3(self, num: int) -> int:
        if(num<=9):return 1
        # count,tmp=0,num
        # while(tmp!=0):
        #     count+=1
        #     tmp=int(tmp/10)
        if(num%100<=25 and num%100-num%10!=0):a,b=1,1
        else:a,b=0,1
        num=int((num-num%10)/10)
        # for i in range(1,count):
        while(num!=0):
            if(num%100<=25 and num%100-num%10!=0):b,a=a+b,b
            else:b,a=a+b,0
            num=int((num-num%10)/10)
        return b
    # 答案
    def translateNum(self,num:int)->int:
        a = b = 1
        y = num % 10
        while num > 9:
            num //= 10
            x = num % 10
            tmp = 10 * x + y
            c = a + b if 10 <= tmp <= 25 else a
            a, b = c, a
            y = x
        return a





if __name__=="__main__":
    S=Solution()
    # print(S.translateNum1(1001))
    # print(S.translateNum2(1001))
    print(S.translateNum3(1001))
    # print(S.translateNum1(1001221234))
    # print(S.translateNum2(1001221234))
    # print(S.translateNum3(1001221234))
    # print(S.translateNum1(22121212))
    # print(S.translateNum2(22121212))
    # print(S.translateNum3(22121212))