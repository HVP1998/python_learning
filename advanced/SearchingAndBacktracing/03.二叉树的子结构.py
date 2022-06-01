'''
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
B是A的子结构，即A中有出现和B相同的结构和节点值。
'''
"""
原始方法：DFS+前序遍历、BFS+层序遍历
遍历A树的每一个节点node_A，以node_A为根判断结构是否和B相同
上述方法速度快占用空间资源多

-------------------------------------------------------

答案精进：
将对二叉树的遍历进行整理不用额外的空间
原始方法是考虑通过队列对二叉树实现遍历，是考虑将左叶子节点、右叶子节点、根统一化，调用函数的时候不用再进行区分。
答案将根、左叶子节点、右叶子节点分开实现了代码与空间资源的精简
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # 利用对二叉树的遍历
    def isSubStructure_DFS(self, A:TreeNode, B:TreeNode)->bool:
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        def dfs(na:TreeNode,nb:TreeNode):
            # 边界判断
            if(nb==None):return True
            if(na==None):return False
            if(na.val==nb.val):
                res=dfs(na.left,nb.left) and dfs(na.right,nb.right)
            else:
                return False
            return res
        
        if(B==None):return False
        stack=[]
        while(A or len(stack)>0):
            while(A):
                if(dfs(A,B)):
                    return True
                stack.append(A)
                A=A.left
            node=stack.pop()
            A=node.right
        return False
    def isSubStructure_BFS(self, A:TreeNode, B:TreeNode)->bool:
        
        """
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        """
        def bfs(na:TreeNode,nb:TreeNode):
            # 边界判断
            if(nb==None):return True
            if(na==None):return False
            if(na.val==nb.val):
                res=bfs(na.left,nb.left) and bfs(na.right,nb.right)
            else:
                return False
            return res

        # 层序遍历
        if(B==None):return False
        queue=[A]
        while(len(queue)>0):
            node=queue.pop()
            if(bfs(node,B)):return True
            if(node.left):queue.append(node.left)
            if(node.right):queue.append(node.right)
        return False
    # 答案 
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def recur(A, B):
            # 当B搜索到最后的时候返回true
            if not B: return True
            # 当A为None，当前节点与B不匹配，返回false
            if not A or A.val != B.val: return False
            # 深度优先搜索
            return recur(A.left, B.left) and recur(A.right, B.right)
        # 将层序遍历整合
        return bool(A and B) and (recur(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))


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
    print(S.isSubStructure_DFS(node0,Node0))