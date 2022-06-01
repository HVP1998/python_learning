'''
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。
'''


class ListNode:
    def __init__(self, value) -> None:
        self.val = value
        self.next = None


class Solution:
    # 递归
    def reversePrint1(self, head: ListNode) -> list[int]:
        return self.reversePrint1(head.next)+[head.val] if head else []
    
    # 利用栈输出
    def reversePrint2(self, head: ListNode) -> list[int]:
        stack = []
        while(head):
            stack.append(head.val)
            head = head.next
        return stack[::-1]


if __name__ == "__main__":
    head = ListNode(1)
    middle = ListNode(2)
    end = ListNode(3)
    head.next = middle
    middle.next = end
    S = Solution()
    nums1 = S.reversePrint1(head)
    print(nums1)
    nums2 = S.reversePrint2(head)
    print(nums2)
