'''
给你二叉树的根节点 root 和一个整数目标和 targetSum ，找出所有 从根节点到叶子节点 路径总和等于给定目标和的路径。

叶子节点 是指没有子节点的节点。
'''
"""      
注意：
res.append(list(path))将path的值作为新的变量入队，而非res.append(path)
因为当path的值改变时由于res.append(path)入队的是path对象res也会改变
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum_DFS(self, root: TreeNode, target: int) -> list[list[int]]:
        def dfs(cur:TreeNode,sum:int,tmp:list,res:list[list[int]]):
            # 数据记录
            tmp.append(cur.val)
            sum+=cur.val
            # 边界判断：二叉树触底返回
            if(not cur.left and not cur.right):
                if(sum==target):
                    # 此处创建了新的列表而不是用tmp
                    # 因为使用tmp是引用传递，当tmp值发生改变会对res造成影响
                    res.append(list(tmp))
                return res
            # 深度搜索
            if(cur.left):
                res=dfs(cur.left,sum,tmp,res)
                tmp.pop()
            if(cur.right):
                res=dfs(cur.right,sum,tmp,res)
                tmp.pop()
            return res
        if(not root):return []
        return dfs(root,0,[],[])
    # 答案精进
    def pathSum(self, root: TreeNode, target: int) -> list[list[int]]:
        res, path = [], []
        def recur(root, tar):
            if not root: return
            path.append(root.val)
            tar -= root.val
            if tar == 0 and not root.left and not root.right:
                res.append(list(path))
            recur(root.left, tar)
            recur(root.right, tar)
            path.pop()

        recur(root, sum)
        return res

           
            


if __name__=="__main__":    
    node0=TreeNode(5)
    node1=TreeNode(4)
    node2=TreeNode(8)
    node0.left=node1
    node0.right=node2
    node3=TreeNode(11)
    node4=TreeNode(13)
    node5=TreeNode(4)
    node1.left=node3
    node2.left=node4
    node2.right=node5
    node6=TreeNode(7)
    node7=TreeNode(2)
    node8=TreeNode(5)
    node9=TreeNode(1)
    node3.left=node6
    node3.right=node7
    node5.left=node8
    node5.right=node9

    Node1=TreeNode(1)
    Node2=TreeNode(2)
    Node1.left=Node2

    S=Solution()
    # print(S.levelOrder_listandlist(node0))
    # print(S.levelOrder_listanddict(node0))
    print(S.pathSum_DFS(node0,22))