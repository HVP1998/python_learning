'''
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印
'''
"""
BFS

-------------------------------------------------------

答案精进：
利用当前队列的长度为循环结束的条件，省去了额外空间资源
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 双列表
    def levelOrder_listandlist(self, root: TreeNode) -> list[list]:
        # 空二叉树返回空列表
        if(not root):return []
        # 初始化数据，利用双列表区分每层节点
        # queue1中存储本层节点，queue2存储下层节点，tmp为本层节点值，res为最后结果
        queue1,queue2,tmp,res=[root],[],[],[]
        # 当双列表都没有数据时说明二叉树层序遍历完成
        while(len(queue1) or len(queue2)):
            # 遍历本层节点
            while(len(queue1)):
                cur=queue1.pop(0)
                # 记录本层节点值
                tmp.append(cur.val)
                # 记录下层节点
                if(cur.left):queue2.append(cur.left)
                if(cur.right):queue2.append(cur.right)
            res.append(tmp)
            # 更新数据以备下一次循环
            queue1,queue2,tmp=queue2,[],[]
        return res
    # 列表+字典
    def levelOrder_listanddict(self, root: TreeNode) -> list[list]:
        # 当为空树时返回[]
        if(not root):return []
        # 数据初始化
        # queue：层序遍历所有节点
        # dic_tree：存储当前节点层数
        # tmp：存储本层节点值
        # level：当前层级
        # res：最后结果
        queue,dic_tree,tmp,res,level=[root],{root:1},[],[],1
        # 层序遍历
        while(len(queue)):
            # 取一个节点
            cur=queue.pop(0)
            # 当左子节点存在
            if(cur.left):
                # 左子节点入队列
                queue.append(cur.left)
                # 记录左子节点层级
                dic_tree[cur.left]=dic_tree[cur]+1
            # 当右子节点存在
            if(cur.right):
                # 右子节点入队列
                queue.append(cur.right)
                # 记录右子节点层级
                dic_tree[cur.right]=dic_tree[cur]+1
            # 当前节点层级大于记录层级说明level层记录完成
            if(dic_tree[cur]>level):
                # 将level层节点数值构成的队列tmp加入队列res
                res.append(tmp)
                # 清空列表以备记录下一层数据
                tmp=[]
                # 更新层级
                level+=1
            # 记录当前节点数值
            tmp.append(cur.val)
        # 由于最后一层记录完成后直接退出循环所以进行一次额外的入队操作
        res.append(tmp)
        return res
    # 答案精进：单列表
    def levelOrder_list(self, root: TreeNode) -> list[list]:
        # 空二叉树返回空列表
        if(not root):return []
        # 初始化数据，利用双列表区分每层节点
        # queue1中存储本层节点，queue2存储下层节点，tmp为本层节点值，res为最后结果
        queue,tmp,res=[root],[],[]
        # 当双列表都没有数据时说明二叉树层序遍历完成
        while(len(queue)):
            # 遍历本层节点
            for _ in range(len(queue)):
                cur=queue.pop(0)
                # 记录本层节点值
                tmp.append(cur.val)
                # 记录下层节点
                if(cur.left):queue.append(cur.left)
                if(cur.right):queue.append(cur.right)
            res.append(tmp)
            # 更新数据以备下一次循环
            tmp=[]
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

    S=Solution()
    # print(S.levelOrder_listandlist(node0))
    # print(S.levelOrder_listanddict(node0))
    print(S.levelOrder_list(node0))