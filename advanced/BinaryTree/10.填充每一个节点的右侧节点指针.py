'''
给定一个完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。
如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL
'''
"""
层序遍历+双列表
层序遍历+成员为元组的列表
层序遍历+成员为列表的列表
-------------------------------------------------------------------
答案精进：
利用next实现常数级空间占用（迭代，递归）
"""
# Definition for a Node.
class TreeNode:
    def __init__(self, val: int = 0, left: 'TreeNode' = None, right: 'TreeNode' = None, next: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # 层序遍历+双列表
    def connect(self, root:TreeNode) -> TreeNode:
        if(not root):return root
        queue=[root]
        while(len(queue)>0):
            tmp=[]
            while(len(queue)>0):
                cur=queue.pop(0)
                if(queue):
                    cur.next=queue[0]
                if(cur.left):tmp.append(cur.left)
                if(cur.right):tmp.append(cur.right)
            queue=tmp
        return root
    # 层序遍历+成员为元组的列表
    def connect(self, root:TreeNode) -> TreeNode:
        if(not root):return root
        queue=[(root,0)]
        while(len(queue)>0):
            cur1,depth1=queue.pop(0)
            if(len(queue)>0):
                cur2,depth2=queue[0]
                if(depth1==depth2):cur1.next=cur2
            if(cur1.left):queue.append((cur1.left,depth1+1))
            if(cur1.right):queue.append((cur1.right,depth1+1))
        return root
    # 层序遍历+成员为列表的列表
    def connect(self, root:TreeNode) -> TreeNode:
        if(not root):return root
        queue,i=[[root]],0
        while(len(queue[i])>0):
            queue.append([])
            for _ in range(len(queue[i])):
                cur=queue[i].pop(0)
                if(len(queue[i])>0):cur.next=queue[i][0]
                if(cur.left):queue[i+1].append(cur.left)
                if(cur.right):queue[i+1].append(cur.right)
            i+=1
        return root
    # 答案精进：迭代
    def connect_answer1(self, root:TreeNode) -> TreeNode:
        cur=root
        while(cur.left):
            tmp=cur
            cur.left.next=cur.right
            while(cur.next):
                cur.right.next=cur.next.left
                cur=cur.next
                cur.left.next=cur.right
            cur=tmp.left
        return root
    # 答案精进：递归
    def connect_answer2(self, root:TreeNode) -> TreeNode:
        def DLR(cur:TreeNode):
            if(not cur.left):return
            cur.left.next=cur.right
            if(cur.next):
                cur.right.next=cur.next.left
            DLR(cur.left)
            DLR(cur.right)
            return 
        DLR(root)
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
    S=Solution()
    print(S.connect_answer1(node0))