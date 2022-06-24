'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
'''
"""
DLR+双列表
DLR+单列表
-------------------------------------------------------------
答案精进：
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # DLR+双列表
    def lowestCommonAncestor1(self, root:TreeNode, p:TreeNode, q:TreeNode) ->TreeNode:
        def DLR(cur:TreeNode,target:TreeNode,l:list):
            if(not cur or len(self.tmp)>0):return
            l.append(cur)
            if(cur==target):
                self.tmp=list(l)
                return 
            DLR(cur.left,target,l)
            DLR(cur.right,target,l)
            l.pop()
            return 
        # 当节点为根节点或为空树
        if(not root or q==root or p==root):return root
        # 存储路径
        self.tmp=[]
        DLR(root,p,[])
        # p节点的路径
        p_path=list(self.tmp)
        # 清空列表用于下一次存储
        self.tmp=[]
        DLR(root,q,[])
        # q节点的路径
        q_path=list(self.tmp)
        # 寻找最后一个相同的路径节点
        for i in range(1,min(len(p_path),len(q_path))):
            if(p_path[i]!=q_path[i]):return p_path[i-1]
        return p_path[min(len(p_path),len(q_path))-1] 
    # DLR+单列表
    def lowestCommonAncestor2(self, root:TreeNode, p:TreeNode, q:TreeNode) ->TreeNode:
        def path(cur:TreeNode,target_p:TreeNode,target_q:TreeNode,l:list):
            if(not cur or len(self.path)>0):return
            l.append(cur)
            if(cur==target_p):
                self.path,self.sign=list(l),'p'
                return 
            if(cur==target_q):
                self.path,self.sign=list(l),'q'
                return 
            path(cur.left,target_p,target_q,l)
            path(cur.right,target_p,target_q,l)
            l.pop()
        def common(cur:TreeNode,target:TreeNode):
            if(not cur or cur in self.path):return False
            if(cur==target):return True
            return common(cur.left,target) or common(cur.right,target)

        if(not root or p==root or q==root):return root
        self.path,self.sign=[],''
        path(root,p,q,[])
        for i in range(len(self.path)-1,0,-1):
            if(self.sign=='p'):
                if(common(self.path[i].left,q) or common(self.path[i].right,q)):return self.path[i]
            if(self.sign=='q'):
                if(common(self.path[i].left,p) or common(self.path[i].right,p)):return self.path[i]
        return self.path[0]
    # 答案精进
    def lowestCommonAncestor_answer(self, root:TreeNode, p:TreeNode, q:TreeNode) ->TreeNode:
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor_answer(root.left, p, q)
        right = self.lowestCommonAncestor_answer(root.right, p, q)
        if not left: return right
        if not right: return left
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
    S=Solution()
    print(S.lowestCommonAncestor3(node0,node8,node1))