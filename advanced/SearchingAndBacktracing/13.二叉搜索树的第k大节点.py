'''
给定一棵二叉搜索树，请找出其中第 k 大的节点的值。
'''
"""
中序遍历RDL（递归）+列表
中序遍历RDL（循环）
-----------------------------------------------------------
答案精进：利用self.k和self.res解决递归中局部变量的问题
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 利用RDL中序遍历(递归)得到递减队列，缺点是会占用过多空间资源
    def kthLargest_RDL_RECUR(self, root: TreeNode, k: int) -> int:
        def RDL_recur(cur,num):
            if(not cur):return
            RDL_recur(cur.right,num)
            if(len(res)==k):return
            res.append(cur.val)
            RDL_recur(cur.left,num)
        res=[]
        RDL_recur(root,1)
        return res[k-1]
    # 利用RDL中序遍历(循环)，可以省去递归中的额外空间
    def kthLargest_RDL_LOOP(self, root: TreeNode, k: int) -> int:
        if(not root):return 0
        stack,num,cur=[],0,root
        while(cur or len(stack)):
            while(cur):
                stack.append(cur)
                cur=cur.right
            cur=stack.pop()
            num+=1
            if(num==k):return cur.val
            cur=cur.left
    # 答案精进
    def kthLargest_answer(self, root: TreeNode, k: int) -> int:
        def RDL_recur(cur):
            if(not cur):return
            RDL_recur(cur.right)
            self.num+=1
            if(self.num==k):
                self.res=cur.val
                return
            RDL_recur(cur.left)
        self.num,self.res=0,0
        RDL_recur(root)
        return self.res

        
        


if __name__=="__main__":    
    node0=TreeNode(0)
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(3)
    node4=TreeNode(4)
    node5=TreeNode(5)
    node6=TreeNode(6)
    node7=TreeNode(7)
    node8=TreeNode(8)
    node9=TreeNode(9)
    node10=TreeNode(10)
    node11=TreeNode(11)
    node12=TreeNode(12)
    node13=TreeNode(13)
    node14=TreeNode(14)
    node7.left=node3
    node7.right=node11
    node3.left=node1
    node3.right=node5
    node11.left=node9
    node11.right=node13
    node1.left=node0
    node1.right=node2
    node5.left=node4
    node5.right=node6
    node9.left=node8
    node9.right=node10
    node13.left=node12
    node13.right=node14

    S=Solution()
    # print(S.kthLargest_RDL_RECUR(node7,10))
    print(S.kthLargest_RDL_LOOP(node7,10))