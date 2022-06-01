'''
给定一个m×n的二维字符网格board和字符word
如果word存在于网格board中返回true否则返回false
单词必须按照字母顺序，通过相邻的单元格内的字母构成，
其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母不允许被重复使用。
'''
"""
答案精进：深度优先搜索(DFS)+剪枝
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # DFS deep first search 深度优先搜索
        def dfs(i,j,k):
            #当(1)索引范围超出界限(2)当前字符不匹配，返回False
            if not 0<=i<len(board) or not 0<=j<len(board[0]) or not board[i][j]==word[k]:return False
            #当前字符是word中最后一个字符返回True，完成匹配
            if k==len(word)-1:return True
            # 当前矩阵中字符标记表明识别过
            board[i][j]=""
            # 通过或的关系计算
            res=dfs(i+1,j,k+1) or dfs(i,j+1,k+1) or dfs(i-1,j,k+1) or dfs(i,j-1,k+1)
            # 恢复识别过的字符
            # 如果当前识别序列中出现不匹配，必须保证恢复矩阵原数据，保证下一次识别的准确性
            board[i][j]=word[k]
            return res
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0): return True
        return False