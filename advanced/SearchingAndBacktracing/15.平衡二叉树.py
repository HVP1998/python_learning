'''
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。
如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。
'''
"""
DFS+BTT
DFS+TTB
BFS+单列表
BFS+双列表
----------------------------------------------------------------------
答案精进：
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # DFS+BTT
    def isBalanced_DFS_BTT(self, root: TreeNode) -> bool:
        # 计算树的深度(BTT)
        def max_depth(cur:TreeNode)->int:
            if(not cur):return 0
            return 1+max(max_depth(cur.left),max_depth(cur.right))
        # 判断平衡二叉树
        def isbalatree(cur:TreeNode)->bool:
            if(not cur):return True
            if(abs(max_depth(cur.left)-max_depth(cur.right))>1):return False
            else:return isbalatree(cur.left) and isbalatree(cur.right)
        if(not root):return True
        return isbalatree(root)
    # DFS+TTB
    def isBalanced_DFS_TTB(self, root: TreeNode) -> bool:
        # 计算树的深度(TTB)
        def max_depth(cur:TreeNode,depth:int)->int:
            if(not cur):
                self.max=max(depth-1,self.max)
                return
            max_depth(cur.left,depth+1)
            max_depth(cur.right,depth+1)
            return
        # 判断平衡二叉树
        def isbalatree(cur:TreeNode)->bool:
            if(not cur):return True
            self.max=0
            max_depth(cur.left,1)
            left_depth=self.max
            self.max=0
            max_depth(cur.right,1)
            right_depth=self.max
            if(abs(right_depth-left_depth)>1):return False
            return isbalatree(cur.left) and isbalatree(cur.right)
        if(not root):return True
        self.max=0
        return isbalatree(root)
    # BFS+单列表
    def isBalanced_BFS(self, root: TreeNode) -> bool:
        # 计算树的深度(单列表BFS)
        def max_depth(cur:TreeNode)->int:
            if(not cur):return 0
            queue,res=[(cur,1)],0
            while(len(queue)):
                node,depth=queue.pop(0)
                res=max(res,depth)
                if(node.left):queue.append((node.left,depth+1))
                if(node.right):queue.append((node.right,depth+1))
            return res
        # 判断平衡二叉树
        def isbalatree(cur:TreeNode)->bool:
            if(not cur):return True
            if(abs(max_depth(cur.left)-max_depth(cur.right))>1):return False
            else:return isbalatree(cur.left) and isbalatree(cur.right)
        if(not root):return True
        return isbalatree(root)
    # BFS+双列表
    def isBalanced_BFS(self, root: TreeNode) -> bool:
        # 计算树的深度(双列表BFS)
        def max_depth(cur:TreeNode)->int:
            if(not cur):return 0
            queue,res=[cur],0
            while(len(queue)):
                tmp=[]
                res+=1
                while(len(queue)):
                    node=queue.pop(0)
                    if(node.left):tmp.append(node.left)
                    if(node.right):tmp.append(node.right)
                queue=tmp
            return res
        # 判断平衡二叉树
        def isbalatree(cur:TreeNode)->bool:
            if(not cur):return True
            if(abs(max_depth(cur.left)-max_depth(cur.right))>1):return False
            else:return isbalatree(cur.left) and isbalatree(cur.right)
        if(not root):return True
        return isbalatree(root)
    # 答案精进
    def isBalanced_answer(self, root: TreeNode) -> bool:
        # 计算树的深度(双列表BFS)
        def max_depth(cur:TreeNode)->int:
            if(not cur):return 0
            queue,res=[cur],0
            while(len(queue)):
                tmp=[]
                res+=1
                while(len(queue)):
                    node=queue.pop(0)
                    if(node.left):tmp.append(node.left)
                    if(node.right):tmp.append(node.right)
                queue=tmp
            return res
        # 判断平衡二叉树
        def isbalatree(cur:TreeNode)->bool:
            if(not cur):return True
            return abs(max_depth(cur.left)-max_depth(cur.right))<=1 \
                and isbalatree(cur.left) and isbalatree(cur.right)
        return isbalatree(root)
