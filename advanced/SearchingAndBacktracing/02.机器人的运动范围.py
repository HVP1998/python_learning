'''
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。
一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），
也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
但它不能进入方格 [35, 38]，因为3+5+3+8=19。
请问该机器人能够到达多少个格子？
'''
"""
DFS：
取各个位：sum+=int(row%10),sum+=int(col%10)
判断边界：sum>max
数据记录：res+=1
继续搜索：dfs(row,col)
以上为错误思路
错误原因：没有考虑数值上满足条件但是空间上无法到达的点

-------------------------------------------------------

答案精进：

DFS：

BFS:
"""
class Solution_error(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        def dfs(row,col,res)->int:
            sum=0
            row_tmp=row
            col_tmp=col
            while(row_tmp!=0):
                sum+=row_tmp%10
                row_tmp=int(row_tmp/10)
            while(col_tmp!=0):
                sum+=col_tmp%10
                col_tmp=int(col_tmp/10)
            if(col>n-1):return res
            if(sum<=k):res+=1
            res=dfs(row,col+1,res)
            return res
        
        res_new=0
        for i in range(m):
            res_new+=dfs(i,0,0)
        return res_new
class Solution:
    #DFS
    def movingCount_DFS(self, m: int, n: int, k: int) -> int:
        
        def dfs(i,j,si,sj):
            # 边界判断
            if(i>m-1 or j>n-1 or si+sj>k or (i,j) in visited):return 0
            # 数据记录
            visited.add((i,j))
            # 深度优先搜索+数值返回
            return 1+dfs(i,j+1,si,sj+1 if (j+1)%10 else sj-8)+dfs(i+1,j,si+1 if (i+1)%10 else si-8,sj)


        visited=set()
        return dfs(0,0,0,0)


    #BFS
    def movingCount_BFS(self, m: int, n: int, k: int) -> int:
        
        def bfs():
            while(len(queue)>0):
                # 取当前坐标与坐标各位和
                i,j,si,sj=queue.pop(0)
                # 边界判断
                if(i>m-1 or j>n-1 or si+sj>k or (i,j) in visited):continue
                # 记录数据
                visited.add((i,j))
                # 更新列表
                queue.append((i,j+1,si,sj+1 if (j+1)%10 else sj-8))
                queue.append((i+1,j,si+1 if (i+1)%10 else si-8,sj))
            return len(visited)


        queue=[(0,0,0,0)]
        visited=set()
        return bfs()




if __name__=="__main__":
    S=Solution()
    print(S.movingCount_DFS(11,11,9))
    print(S.movingCount_BFS(11,11,9))
        
