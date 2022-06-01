'''
在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值（价值大于0）。你可以从棋盘的左上角开始拿格子里的礼物，
并每次向右或者向下移动一格、直到到达棋盘的右下角。给定一个棋盘及其上面的礼物的价值。请计算你最多能拿到多少价值的礼物
'''
"""
最优子结构

状态定义：
dp[i][j]    从g[i][j]出发到达终点的最大累计值
g[i][j]     第i行j列格的价值
状态转移方程：
dp[i][j]=max(dp[i][j+1]+g[i][j],dp[i+1][j]+g[i][j])   

-------------------------------------------------------

答案精进：
dp[i][j]    从左上角到达g[i][j]时的最大累计值

dp[i][j]=g[i][j]                                    (i==0)and(j==0)
dp[i][j]=dp[i][j-1]+g[i][j]                         (i==0)and(0<j<len(g[0]))
dp[i][j]=dp[i-1][j]+g[i][j]                         (0<i<len(g))and(j==0)
dp[i][j]=max(dp[i][j-1]+g[i][j],dp[i-1][j]+g[i][j]) (0<i<len(g))and(0<j<len(g[0]))
"""

class Solution:
    # 暴力递归
    def maxValue1(self,grid:list[list[int]]) -> int:
        m,n,grid_sub=len(grid),len(grid[0]),[]
        f_n=grid[0][0]
        if(m==1):
            for i in range(1,n):
                f_n=f_n+grid[m-1][i]
            return f_n
        elif(n==1):
            for i in range(1,m):
                f_n=f_n+grid[i][n-1]
            return f_n
        for i in range(0,m):
            grid_sub.append(grid[i][1:n])
        f_n_right=self.maxValue1(grid_sub)
        f_n_down=self.maxValue1(grid[1:m])
        f_n=max(f_n+f_n_right,f_n+f_n_down)
        return f_n
    # 记忆化递归
    def maxValue2(self,grid:list[list[int]]) -> int:
        m,n=len(grid),len(grid[0])
        f_n=grid[0][0]
        if(m==1):
            for i in range(1,n):
                f_n=f_n+grid[m-1][i]
            return f_n
        elif(n==1):
            for i in range(1,m):
                f_n=f_n+grid[i][n-1]
            return f_n
        else:
            memory=[]
            for i in range(0,m):
                memory.append([0]*n)
            return self.MemoRecru(grid,memory)
    def MemoRecru(self,grid:list[list[int]],memory:list[list[int]]):
        m,n,f_n,grid_sub=len(grid),len(grid[0]),grid[0][0],[]
        if(m==1):
            for i in range(1,n):
                f_n=f_n+grid[m-1][i]
            return f_n
        elif(n==1):
            for i in range(1,m):
                f_n=f_n+grid[i][n-1]
            return f_n
        if(memory[len(memory)-m][len(memory[0])-n]!=0):return memory[len(memory)-m][len(memory[0])-n] 
        for i in range(0,m):
            grid_sub.append(grid[i][1:n])
        memory[len(memory)-m][len(memory[0])-n+1]=self.MemoRecru(grid_sub,memory)
        memory[len(memory)-m+1][len(memory[0])-n]=self.MemoRecru(grid[1:m],memory)
        f_n=max(f_n+memory[len(memory)-m][len(memory[0])-n+1],f_n+memory[len(memory)-m+1][len(memory[0])-n])
        return f_n
    # 动态规划
    def maxValue3(self,grid:list[list[int]]):
        m,n,f_n=len(grid),len(grid[0]),grid[0][0]
        if(m==1):
            for i in range(1,n):
                f_n=f_n+grid[m-1][i]
            return f_n
        elif(n==1):
            for i in range(1,m):
                f_n=f_n+grid[i][n-1]
            return f_n
        memory=[]
        for i in range(0,m):
            memory.append([0]*n)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if(j==n-1 and i==m-1):
                    memory[i][j]=grid[i][j]
                elif(j==n-1):
                    memory[i][j]=memory[i+1][j]+grid[i][j]
                elif(i==m-1):
                    memory[i][j]=memory[i][j+1]+grid[i][j]
                else:
                    memory[i][j]=max(memory[i+1][j]+grid[i][j],memory[i][j+1]+grid[i][j])
        return memory[0][0]
    # 答案
    def maxValue(self,grid:list[list[int]]):
        # 数组第一行第一列预处理
        for i in range(1,len(grid)):
            grid[i][0]=grid[i-1][0]+grid[i][0]
        for i in range(1,len(grid[0])):
            grid[0][i]=grid[0][i-1]+grid[0][i]
        for i in range(1,len(grid)):
            for j in range(1,len(grid[0])):
                grid[i][j]=grid[i][j]+max(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]


if __name__=="__main__":
    S=Solution()
    # print(S.maxValue1([[1,3,1],[1,5,1],[4,2,1]]))
    # print(S.maxValue2([[1,3,1],[1,5,1],[4,2,1]]))
    # print(S.maxValue3([[1,3,1],[1,5,1],[4,2,1]]))
    print(S.maxValue([[1,3,1],[1,5,1],[4,2,1]]))
    # print(S.maxValue1([[1,3,12,5],[1,7,5,1],[4,2,1,8]]))
    # print(S.maxValue2([[1,3,12,5],[1,7,5,1],[4,2,1,8]]))
    # print(S.maxValue3([[1,3,12,5],[1,7,5,1],[4,2,1,8]]))
    print(S.maxValue([[1,3,12,5],[1,7,5,1],[4,2,1,8]]))