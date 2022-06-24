'''

'''
"""

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 递归
    def inorderTraversal_recur(self, root: TreeNode) -> list[int]:
        def dlr(cur:TreeNode):
            if(not cur):return
            dlr(cur.left)
            self.res.append(cur.val)
            dlr(cur.right)
            return 

        self.res=[]
        dlr(root)
        return self.res
    # 循环
    def inorderTraversal_loop(self, root: TreeNode) -> list[int]:
        tmp,res,cur=[],[],root
        while(cur or len(tmp)):
            while(cur):
                tmp.append(cur)
                cur=cur.left
            cur=tmp.pop()
            res.append(cur.val)
            cur=cur.right
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
    print(S.inorderTraversal_recur(node0))
    print(S.inorderTraversal_loop(node0))