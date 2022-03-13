'''
实现 copyRandomList 函数,复制一个复杂链表。在复杂链表中,每个节点除了有一个 next 指针指向下一个节点,还有一个 random 指针指向链表中的任意节点或者 null。
'''
class Node:
    def __init__(self, x: int, next: 'Node'= None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: Node) -> Node:
        # Node with label 7 was not copied but a reference to the original one.
        # 此方法不行的原因是直接引用了原来的链表，😓
        # new_head=tmp_head=head
        # while(head):
        #     head=head.next
        #     tmp_head.next=head
        #     tmp_head=tmp_head.next
        # return new_head
        # ************************************************************************
        # Random pointer of node with val 13 points to a node not in the copied list
        # pre=head
        # cur=head.next
        # dict_Node=dict()
        # dict_Node[head]=Node(head.val)
        # while(cur):
        #     dict_Node[cur]=Node(cur.val)
        #     dict_Node[pre].next=dict_Node[cur]
        #     pre=cur
        #     cur=cur.next
        # cur=head
        # while(cur):
        #     if(not cur.random==None):
        #出错原因在于在字典中创建好链表节点后应当使用字典中的节点而非再创建节点
        #         dict_Node[cur].random=Node(cur.random.val)
        #     else:
        #         dict_Node[cur].random=None
        #     cur=cur.next
        # return dict_Node[head]
        #  ************************************************************************
        # pre=head
        # cur=head.next
        # dict_Node=dict()
        # dict_Node[head]=Node(head.val)
        # while(cur):
        #     dict_Node[cur]=Node(cur.val)
        #     dict_Node[pre].next=dict_Node[cur]
        #     pre=cur
        #     cur=cur.next
        # cur=head
        # while(cur):
        #     dict_Node[cur].random=dict_Node.get(cur.random)
        #     cur=cur.next
        # return dict_Node[head]
        # **********************************************************************
        # if not head: return
        # cur = head
        # # 1. 复制各节点，并构建拼接链表
        # while cur:
        #     tmp = Node(cur.val)
        #     tmp.next = cur.next
        #     cur.next = tmp
        #     cur = tmp.next
        # # 2. 构建各新节点的 random 指向
        # cur = head
        # while cur:
        #     if cur.random:
        #         cur.next.random = cur.random.next
        #     cur = cur.next.next
        # # 3. 拆分两链表
        # cur = res = head.next
        # pre = head
        # while cur.next:
        #     pre.next = pre.next.next
        #     cur.next = cur.next.next
        #     pre = pre.next
        #     cur = cur.next
        # pre.next = None # 单独处理原链表尾节点
        # return res      # 返回新链表头节点
        # ************************************************************************
        if not head: return
        dic = {}
        # 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        # 4. 构建新节点的 next 和 random 指向
        while cur:
            dic[cur].next = dic.get(cur.next)
            dic[cur].random = dic.get(cur.random)
            cur = cur.next
        # 5. 返回新链表的头节点
        return dic[head]
    def showNode(self,head:Node)->Node:
        while(head):
            print("Node.val:",head.val)
            if(head.next):
                print("Node.next:",head.next.val)
            else:
                print("Node.next:",None)
            if(head.random):
                print("Node.random:",head.random.val)
            else:
                print("Node.random:",None)
            print("****************************")
            head=head.next

# [[7,null],[13,0],[11,4],[10,2],[1,0]]
n1=Node(7)
n2=Node(13)
n3=Node(11)
n4=Node(10)
n5=Node(1)
n1.next=n2
n1.random=None
n2.next=n3
n2.random=n1
n3.next=n4
n3.random=n5
n4.next=n5
n4.random=n3
n5.random=n1
S=Solution()
head=S.copyRandomList(n1)
S.showNode(head)