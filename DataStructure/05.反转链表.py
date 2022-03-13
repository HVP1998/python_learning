class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 利用列表的可逆性
    def reverseList1(self, head: ListNode) -> ListNode:
        if(head==None):
            return head
        stack=list()
        while(head):
            stack.append(head)
            head=head.next
        if(len(stack)==1):
            return stack[0]
        stack=stack[::-1]
        for i in range(0,len(stack)-1):
            stack[i].next=stack[i+1]
        stack[len(stack)-1].next=None
        return stack[0]
    # 双指针迭代
    def reverseList2(self, head: ListNode) -> ListNode:
        cur,pre=head,None
        while cur:
            # 实现每次从cur指向pre
            cur.next,pre,cur=pre,cur,cur.next
    # 递归
    def reverseList3(self, head: ListNode) -> ListNode:
        def recur(cur, pre):
            if not cur: return pre     
            res = recur(cur.next, cur) 
            cur.next = pre             
            return res                 
        return recur(head, None)       
    
    
        
    def showList(self,head:ListNode)->ListNode:
        while(head):
            print(head.val)
            head=head.next

if __name__=="__main__":
    # LN1=ListNode(1)
    # LN2=ListNode(2)
    # LN3=ListNode(3)
    # LN4=ListNode(4)
    # LN5=ListNode(5)
    # LN1.next=LN2
    # LN2.next=LN3
    # LN3.next=LN4
    # LN4.next=LN5
    LN1=ListNode(None)
    head=LN1
    S=Solution()    
    S.showList(head)
    head=S.reverseList1(head)
    S.showList(head)

