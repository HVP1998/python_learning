'''
输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的循环双向链表。要求不能创建任何新的节点，只能调整树中节点指针的指向。
'''
"""
中序遍历（循环）+队列
------------------------------------------------------------
答案精进：
中序遍历（递归）+双指针
省略了额外的队列空间
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 中序遍历（循环）+队列
    def treeToDoublyList_LDR_loop_queue(self, root: 'Node') -> 'Node':
        # 空树返回根节点
        if(not root):return root
        # 数据初始化
        # stack：栈
        # queue；队列
        # cur：当前节点
        stack,queue,cur=[],[],root
        # 中序遍历
        while(len(stack) or cur):
            while(cur):
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            queue.append(cur)
            cur=cur.right
        # 根据队列中的存储顺序前向连接节点
        for i in range(-1,len(queue)-1,1):
            if(not queue[i].right==queue[i+1]):
                queue[i].right=queue[i+1]
        # 根据队列中的存储顺序后向连接节点
        for i in range(len(queue)-1,0,-1):
            if(not queue[i].left==queue[i-1]):
                queue[i].left=queue[i-1]
        # 两端节点连接
        queue[0].left=queue[-1]
        # 返回头节点
        return queue[0]
    # 答案精进
    # 中序遍历（递归）+双指针
    def treeToDoublyList_LDR_recur_doublepoint(self, root: 'Node') -> 'Node':
        def dfs(cur):
            if not cur: return
            dfs(cur.left) # 递归左子树
            if self.pre: # 修改节点引用
                self.pre.right, cur.left = cur, self.pre
            else: # 记录头节点
                self.head = cur
            self.pre = cur # 保存 cur
            dfs(cur.right) # 递归右子树
        
        if not root: return
        self.pre = None
        dfs(root)
        self.head.left, self.pre.right = self.pre, self.head
        return self.head


if __name__=="__main__":    
    node0=Node(4)
    node1=Node(2)
    node2=Node(6)
    node0.left=node1
    node0.right=node2
    node3=Node(1)
    node4=Node(3)
    node5=Node(5)
    node6=Node(7)
    node1.left=node3
    node1.right=node4
    node2.left=node5
    node2.right=node6


    Node1=Node(1)
    Node2=Node(2)
    Node1.left=Node2
    
    S=Solution()
    print(S.treeToDoublyList_LDR_loop_queue(node0))