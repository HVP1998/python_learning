# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        def recur(root:int,left:int,right:int):
            if(left>right):return None
            cur=TreeNode(preorder[root])
            i=posinorder.get(cur.val)
            # 根据前序DLR的特点：当前根节点后为当前根节点左子树的根节点
            # 根节点位置+1=左子树根节点位置
            # 左子树范围由中序遍历确定
            cur.left=recur(root+1,left,i-1)
            # i-left当前根节点左子树的长度，root当前根节点位置
            # 左子树长度+根节点位置+1=右子树根节点位置
            # 右子树范围由中序遍历确定
            cur.right=recur(root+1+i-left,i+1,right)
            return cur


        posinorder=dict()
        for i in range(len(inorder)):
            posinorder[inorder[i]]=i
        return recur(0,0,len(inorder)-1)