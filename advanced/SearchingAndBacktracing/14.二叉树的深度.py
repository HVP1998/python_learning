'''
输入一棵二叉树的根节点，求该树的深度。
从根节点到叶节点依次经过的节点（含根、叶节点）形成树的一条路径，最长路径的长度为树的深度。
'''
"""
DFS+BTT：深度优先搜索+自下向上（从下向上记录值）
DFS+TTB：深度优先搜索+自上向下（从上向下记录值）
BFS：利用队列
--------------------------------------------------
答案精进：双队列BFS
"""
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # BottomToTop
    def maxDepth_DFS_BTT(self, root: TreeNode) -> int:
        def dfs(cur:TreeNode)->int:
            if(not cur):return 0
            return 1+max(dfs(cur.left),dfs(cur.right))
        return dfs(root)
    # TopToBottom
    def maxDepth_DFS_TTB(self, root: TreeNode) -> int:
        def dfs(cur:TreeNode,depth:int):
            if(not cur):
                self.res=max(self.res,depth)
                return
            dfs(cur.left,depth+1)
            dfs(cur.right,depth+1)
        self.res=0
        dfs(root,0)
        return self.res
    # BFS
    def maxDepth_BFS(self, root: TreeNode) -> int:
        if(not root):return 0
        queue=[(root,1)]
        res=0
        while(len(queue)):
            cur,depth=queue.pop(0)
            if(not cur.left and not cur.right):
                res=max(res,depth)
            if(cur.left):queue.append((cur.left,depth+1))
            if(cur.right):queue.append((cur.right,depth+1))
        return res
    # 答案精进
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue,res=[root],0
        while(len(queue)):
            res+=1
            tmp=[]
            while(len(queue)):
                cur=queue.pop(0)
                if(cur.left):tmp.append(cur.left)
                if(cur.right):tmp.append(cur.right)
            queue=tmp
        return res



if __name__=="__main__":
    node0=TreeNode(0)
    node1=TreeNode(1)
    node2=TreeNode(2)
    node0.left=node1
    node0.right=node2
    node3=TreeNode(3)
    node4=TreeNode(4)
    node5=TreeNode(5)
    node6=TreeNode(6)
    node1.left=node3
    node1.right=node4
    node2.left=node5
    node2.right=node6
    node7=TreeNode(7)
    node8=TreeNode(8)
    node9=TreeNode(9)
    node10=TreeNode(10)
    node11=TreeNode(11)
    node12=TreeNode(12)
    node13=TreeNode(13)
    node14=TreeNode(14)
    node3.left=node7
    node3.right=node8
    node4.left=node9
    node4.right=node10
    node5.left=node11
    node5.right=node12
    node6.left=node13
    node6.right=node14
    S=Solution()
    print(S.maxDepth_BTT(node0))
    print(S.maxDepth_TTB(node0))
