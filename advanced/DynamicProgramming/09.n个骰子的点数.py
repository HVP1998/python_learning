'''
把n个骰子扔在地上，所有骰子朝上一面的点数之和为s。输入n，打印出s的所有可能的值出现的概率。
你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 n 个骰子所能掷出的点数集合中第 i 小的那个的概率。
'''
"""
①
状态定义：
dp[i]   骰子和为i时的概率
dic[o]  第o个骰子为2时的概率
转移方程：
dp[i:j]=dic[o]
②
状态定义
dic[n]  n个骰子的概率
转移方程
dic[n][i]=dic[n-1][i]                                       i==0
dic[n][i]=dic[n][i-1]+dic[n-1][i]/6                         0<i<=5
dic[n][i]=dic[n][i-1]+(dic[n-1][i]-dic[n-1][i-6])/6         5<i<=len(dic[n-1])-1
dic[n][i]=dic[n][i-1]-dic[n-1][i-6]/6                       len(dic[n-1])-1<i<=len(dic[n])-1
-------------------------------------------------------
答案精进：
答案与新方法思路相同
"""
class Solution:
    # 暴力递归：超出时间限制
    def dicesProbability1(self, n: int) -> list[float]:
        num,prob=0,[0]*(5*n+1)
        for i in range(n):
            num+=10**i
        prob[0]=prob[0]+1/(6**n)
        return self.DirectRecru1(n,num,n-1,1,prob)
    # n:骰子个数  num:骰子组成的数字  pos_num:num增加的位数  pos_prob:数组概率加一的位置
    def DirectRecru1(self,n:int,num:int,pos_num:int,pos_prob:int,prob:list[float])->list[float]:
        pos=num
        for i in range(pos_num,-1,-1):
            num=pos+10**i
            prob[pos_prob]+=1/(6**n)
            if(num%10==6):return prob
            elif(num%(10**(i+1))>=6*(10**i)):
                prob=self.DirectRecru1(n,num,i-1,pos_prob+1,prob)
            else:
                prob=self.DirectRecru1(n,num,i,pos_prob+1,prob)
        return prob
    # 记忆化递归
    def dicesProbability2(self, n: int) -> list[float]:
        num,prob,dic=0,[0]*(5*n+1),dict()
        for i in range(n):
            num+=10**i
        prob[0]=prob[0]+1/(6**n)
        dic[1]=[1/(6**n)]*5
        return self.DirectRecru2(n,num,n-1,1,prob,dic)
    # n:骰子个数  num:骰子组成的数字  pos_num:num增加的位数  pos_prob:数组概率加一的位置  dic:字典
    def DirectRecru2(self,n:int,num:int,pos_num:int,pos_prob:int,prob:list[float],dic:dict[list[float]])->list[float]:
        pos,judge=num,False
        for i in range(pos_num,-1,-1):
            num=pos+10**i
            # 判断除了第一个骰子是否存在为2的骰子
            for j in range(1,n):
                # 某个骰子为2
                if(num%(10**j)>=2*(10**(j-1)) and num%(10**j)<=3*(10**(j-1))):
                    judge=True
                    # 存在已计算过的数据
                    if(dic.get(j,False)):
                        for k in range(0,len(dic[j])):
                            prob[pos_prob+k]+=dic[j][k]
                    # 不存在计算过的数据，将当前情况计算后将数据录入字典
                    else:
                        prob[pos_prob]+=1/(6**n)
                        if(num%(10**(i+1))>=6*(10**i)):
                            prob=self.DirectRecru2(n,num,i-1,pos_prob+1,prob,dic)
                        else:
                            prob=self.DirectRecru2(n,num,i,pos_prob+1,prob,dic)
                        dic[j]=prob[pos_prob:len(prob)]
                    break  
                if(num%10==2):return prob
            if(judge):continue
            # 除了第一个骰子外不存在为2的骰子
            prob[pos_prob]+=1/(6**n)
            if(num%(10**(i+1))>=6*(10**i)):
                prob=self.DirectRecru2(n,num,i-1,pos_prob+1,prob,dic)
            else:
                prob=self.DirectRecru2(n,num,i,pos_prob+1,prob,dic)
        return prob
    
    
    # 新方法
    def dicesProbability3(self, n: int) -> list[float]:
        if(n==1):return [1/6]*6
        prob_new=[0]*(6+(n-1)*5)
        prob_last=self.dicesProbability3(n-1)
        prob_new[0]=prob_last[0]/6
        for i in range(1,len(prob_new)):
            if(i<=5):
                prob_new[i]=prob_new[i-1]+prob_last[i]/6
            elif(5<i<=len(prob_last)-1):
                prob_new[i]=prob_new[i-1]+(prob_last[i]-prob_last[i-6])/6
            else:
                prob_new[i]=prob_new[i-1]-prob_last[i-6]/6
        return prob_new
    



            


            





if __name__=="__main__":
    S=Solution()
    # print(S.dicesProbability1(3))
    print(S.dicesProbability2(3))
    print(S.dicesProbability3(3))