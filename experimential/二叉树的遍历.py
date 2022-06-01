class TreeNode:
    def __init__(self,num) -> None:
        self.val=num
        self.left=None
        self.right=None

class Solution():
    # 前序遍历+递归
    def dlr_recur(self,root:TreeNode,res:list):
        if(root==None):return res
        res.append(root.val)
        res=self.dlr_recur(root.left,res)
        res=self.dlr_recur(root.right,res)
        return res
    # 前序遍历+循环
    def dlr_loop(self,root:TreeNode):
        if(root==None):return []
        stack=[]
        queue=[]
        cur=root
        while(cur or len(stack)>0):
            while(cur):
                stack.append(cur)
                queue.append(cur.val)
                cur=cur.left
            node=stack.pop()
            cur=node.right
        return queue
    # 中序遍历+递归
    def ldr_recur(self,root:TreeNode,res:list):
        if(root==None):return res
        res=self.ldr_recur(root.left,res)
        res.append(root.val)
        res=self.ldr_recur(root.right,res)
        return res
    # 中序遍历+循环
    def ldr_loop(self,root:TreeNode):
        if(root==None):return []
        stack,queue,cur=[],[],root
        while(cur or len(stack)>0):
            while(cur):
                stack.append(cur)
                cur=cur.left
            node=stack.pop()
            queue.append(node.val)
            cur=node.right
        return queue
    # 后序遍历+递归
    def lrd_recur(self,root:TreeNode,res:list):
        if(root==None):return res
        res=self.lrd_recur(root.left,res)
        res=self.lrd_recur(root.right,res)
        res.append(root.val)
        return res
    # 后序遍历+循环
    def lrd_loop(self,root:TreeNode):
        if(root==None):return []
        stack,queue,cur=[],[],root
        while(cur or len(stack)>0):
            while(cur):
                stack.append(cur)
                queue.append(cur.val)
                cur=cur.right
            node=stack.pop()
            cur=node.left
        return queue[::-1]
    # 层序遍历I+循环（将二叉树的节点值存储在队列中）
    def levelorder_I(sekf,root:TreeNode):
        if(root==None):return []
        queue,res=[root],[]
        while(len(queue)>0):
            cur=queue.pop(0)
            res.append(cur.val)
            if(cur.left):queue.append(cur.left)   
            if(cur.right):queue.append(cur.right)
        return res   
    # 层序遍历II+循环（将二叉树的每层节点值存储在队列中并将此队列存入队列）
    def levelorder_II(sekf,root:TreeNode):
        if(root==None):return []
        queue1,queue2,res2=[root],[],[]
        while(len(queue2)>0 or len(queue1)>0):
            res1=[]
            while(len(queue1)>0):
                node=queue1.pop(0)
                res1.append(node.val)
                if(node.left):queue2.append(node.left)
                if(node.right):queue2.append(node.right)
            res2.append(res1)
            queue1,queue2=queue2,[]
        return res2
    # 层序遍历III+循环（将二叉树的每层节点值按Z型存储在队列中并将此队列存入队列）
    def levelorder_III(sekf,root:TreeNode):
        if(root==None):return []
        queue1,queue2,res2,sign=[root],[],[],1
        while(len(queue2)>0 or len(queue1)>0):
            res1=[]
            while(len(queue1)>0):
                node=queue1.pop(0)
                res1.append(node.val)
                if(node.left):queue2.append(node.left)
                if(node.right):queue2.append(node.right)
            res2.append(res1[::sign])
            queue1,queue2,sign=queue2,[],-sign
        return res2

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

    node_none=None

    Node0=TreeNode(0)
    Node1=TreeNode(1)
    Node2=TreeNode(2)
    Node0.left=Node1
    Node0.right=Node2
    Node3=TreeNode(3)
    Node5=TreeNode(5)
    Node1.left=Node3
    Node2.left=Node5
    S=Solution()
    # print(S.dlr_recur(node0,[]))
    # print(S.dlr_loop(node0))
    # print(S.ldr_recur(node0,[]))
    # print(S.ldr_loop(node0))
    # print(S.lrd_recur(node0,[]))
    # print(S.lrd_loop(node0))
    # print(S.levelorder_I(node0))
    # print(S.levelorder_II(node0))
    # print(S.levelorder_II(node_none))
    # print(S.levelorder_II(Node0))
    print(S.levelorder_III(node0))
    print(S.levelorder_III(node_none))
    print(S.levelorder_III(Node0))