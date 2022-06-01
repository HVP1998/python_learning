'''
用两个栈实现一个队列。实现它的两个函数 appendTail 和 deleteHead ，分别完成在队列尾部插入整数和在队列头部删除整数的功能。
(若队列中没有元素，deleteHead 操作返回 -1 )
'''
class Solution:
    stack_in,stack_out=[],[]
    def __init__(self) -> None:
        self.stack_in,self.stack_out=[],[]
    def appendTail(self,value)->None:
        self.stack_in.append(value)
    def deleteHead(self)->int:
        if not self.stack_out:
            if not self.stack_in:
                return -1
            else:
                while(self.stack_in):
                    self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop()

if __name__=="__main__":
    S=Solution()
    print(S.deleteHead())
    S.appendTail(1)
    S.appendTail(2)
    S.appendTail(3)
    print(S.deleteHead())
    print(S.deleteHead())
    S.appendTail(4)
    S.appendTail(5)
    print(S.deleteHead())
    print(S.deleteHead())
    print(S.deleteHead())
    print(S.deleteHead())
