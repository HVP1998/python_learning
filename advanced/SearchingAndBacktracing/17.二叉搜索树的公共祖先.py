'''
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
'''
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root:TreeNode, p:TreeNode, q:TreeNode) ->TreeNode:
        if(not root):return 
        if(p.val<root.val and q.val<root.val):return self.lowestCommonAncestor(root.left,p,q)
        elif(p.val>root.val and q.val>root.val):return self.lowestCommonAncestor(root.right,p,q)
        else:return root
        