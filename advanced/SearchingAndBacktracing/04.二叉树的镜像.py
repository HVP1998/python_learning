'''
请完成一个函数，输入一个二叉树，该函数输出它的镜像。
'''
"""
DFS：
边界判断：节点为None返回
深度搜索：搜索当前ltn和rtn的左叶子节点和右叶子节点
数据操作：交换节点并返回

-------------------------------------------------------

答案精进：
原始思路受限于DFS的框架，根本问题还是递归思路，不用再构造额外函数。
也可以利用栈辅助，层序遍历
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def dfs(ltn:TreeNode,rtn:TreeNode):
            if(ltn==None and rtn==None):return rtn,ltn
            if(ltn!=None):ltn.left,ltn.right=dfs(ltn.left,ltn.right)
            if(rtn!=None):rtn.left,rtn.right=dfs(rtn.left,rtn.right)
            return rtn,ltn
        if(root==None or (root.left==None and root.right==None)):return root
        root.left,root.right=dfs(root.left,root.right)
        return root
    # 答案
    def mirrorTree1(self,root:TreeNode)->TreeNode:
        if not root: return
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root
    def mirrorTree2(self, root: TreeNode) -> TreeNode:
        if not root: return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)
            node.left, node.right = node.right, node.left
        return root


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
    node3.left=node7
    node3.right=node8
    node4.left=node9
    node4.right=node10
    node11=TreeNode(11)
    node12=TreeNode(12)
    node13=TreeNode(13)
    node14=TreeNode(14)
    node5.left=node11
    node5.right=node12
    node6.left=node13
    node6.right=node14

    Node0=TreeNode(5)
    Node1=TreeNode(11)
    Node2=TreeNode(12)
    Node0.left=Node1
    Node0.right=Node2

    S=Solution()
    S.mirrorTree(node0)
    dp=[node0]
    while(len(dp)>0):
        cur=dp.pop(0)
        print(cur.val)
        if(cur.left!=None):dp.append(cur.left)
        if(cur.right!=None):dp.append(cur.right)
