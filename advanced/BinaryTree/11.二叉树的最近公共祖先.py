'''
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 当前节点为空或当前节点为两节点中任意一个，返回当前节点
        if(not root or p==root or q==root):return root
        left=self.lowestCommonAncestor(root.left)
        right=self.lowestCommonAncestor(root.right)
        if(not left):return right
        if(not right):return left
        return root