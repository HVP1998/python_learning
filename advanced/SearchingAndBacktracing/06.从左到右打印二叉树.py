'''
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印
'''
"""
BFS\DFS:直接判断对称位的节点(值)是否相等
-------------------------------------------------------
答案精进:
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x 
        self.left = None
        self.right = None

class Solution:
    def levelOrder_BFS(self, root: TreeNode) -> list[int]:
        if(root==None):return []
        queue=[root]
        res=[]
        while(len(queue)>0):
            node=queue.pop(0)
            res.append(node.val)
            if(node.left):queue.append(node.left)
            if(node.right):queue.append(node.right)
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

    Node0=TreeNode(5)
    Node1=TreeNode(11)
    Node2=TreeNode(12)
    Node0.left=Node1
    Node0.right=Node2
    Node3=TreeNode(13)
    Node4=TreeNode(14)
    Node2.left=Node3
    Node2.right=Node4

    S=Solution()
    print(S.levelOrder_BFS(node0))
    print(S.levelOrder_BFS(Node0))
