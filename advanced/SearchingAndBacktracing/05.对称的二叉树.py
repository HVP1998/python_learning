'''
判断一棵二叉树是不是对称的。如果一棵二叉树和它的镜像一样，那么它是对称的。
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
    # DFS
    def isSymmetric_DFS(self, root: TreeNode) -> bool:
        def dfs(ltn:TreeNode,rtn:TreeNode):
            # 当前节点都为None，对称，返回True
            if(ltn==None and rtn==None):return True
            # 当前节点都有val
            if(ltn!=None and rtn!=None):
                # 当前节点val相等深度搜索
                if(ltn.val==rtn.val):
                    return dfs(ltn.left,rtn.right) and dfs(ltn.right,rtn.left)
            # 1.两节点有一个为None；2.两节点都有val但是不相等。返回False
            return False
        
        if(root==None):return True
        return dfs(root.left,root.right)
    # BFS
    def isSymmetric_BFS(self, root: TreeNode) -> bool:
        # 当树为空返回True
        if(root==None):return True
        # 队列初始化
        queue=[root.left,root.right]
        while(len(queue)>0):
            ltn=queue.pop(0)
            rtn=queue.pop(0)
            # 两节点都为None继续搜索
            if(ltn==None and rtn==None):continue
            # 1.有一个节点为None有一个节点有val;2.两节点val不相等,返回False
            if((ltn==None and rtn!=None) or (ltn!=None and rtn==None) or (ltn.val!=rtn.val)):
                return False
            # 广度优先搜索
            queue.append(ltn.left)
            queue.append(rtn.right)
            queue.append(ltn.right)
            queue.append(rtn.left)
        return True
    # 答案精进
    def isSymmetric(self, root: TreeNode) -> bool:
        def recur(L, R):
            if not L and not R: return True
            if not L or not R or L.val != R.val: return False
            return recur(L.left, R.right) and recur(L.right, R.left)

        return not root or recur(root.left, root.right)


if __name__=="__main__":    
    node0=TreeNode(0)
    node1=TreeNode(2)
    node2=TreeNode(2)
    node0.left=node1
    node0.right=node2
    node3=TreeNode(3)
    node4=TreeNode(4)
    node5=TreeNode(4)
    node6=TreeNode(3)
    node1.left=node3
    node1.right=node4
    node2.left=node5
    node2.right=node6
    node7=TreeNode(7)
    node8=TreeNode(8)
    node9=TreeNode(9)
    node10=TreeNode(10)
    node11=TreeNode(11)
    node12=TreeNode(9)
    node13=TreeNode(8)
    node14=TreeNode(7)
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

    S=Solution()
    print(S.isSymmetric_DFS(node0))
    print(S.isSymmetric_BFS(node0))
