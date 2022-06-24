'''
给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。
'''
"""
答案精进：
利用位置作为形参而非列表减少了空间与时间的资源占用
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # 递归
    def buildTree_recur(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        if(len(inorder)==0):return None
        root=TreeNode(postorder.pop(-1))
        for i in range(len(inorder)):
            if(inorder[i]==root.val):break
        root.right=self.buildTree_recur(inorder[i+1:],postorder)
        root.left=self.buildTree_recur(inorder[:i],postorder)
        return root
    # 答案精进
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        def recur(root:int,left:int,right:int):
            if(left>right):return None
            cur=TreeNode(postorder[root])
            i=posinorder.get(cur.val)
            # 根据前序LRD的特点：根节点前为当前根节点右子树的根节点
            # 根节点位置-1=右子树根节点位置
            # 右子树范围由中序遍历确定
            cur.right=recur(root-1,i+1,right)
            # right-i当前根节点左子树的长度，root当前根节点位置
            # 根节点位置-右子树长度-1=右子树根节点位置
            # 右子树范围由中序遍历确定
            cur.left=recur(root-right+i-1,left,i-1)
            return cur


        posinorder=dict()
        for i in range(len(inorder)):
            posinorder[inorder[i]]=i
        return recur(len(posinorder)-1,0,len(inorder)-1)



        
            