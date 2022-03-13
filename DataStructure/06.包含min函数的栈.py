class MinStack:

    # def __init__(self):
    #     self.stack_num=list()
    #     self.stack_min=list()
    # def push(self, x: int) -> None:
    #     self.stack_num.append(x)
    #     if(not self.stack_min):
    #         self.stack_min.append(x)
    #     else:
    #         if(x<=self.stack_min[len(self.stack_min)-1]):
    #             self.stack_min.append(x)
    #         else:
    #             self.stack_min.append(self.stack_min[len(self.stack_min)-1])
    # def pop(self) -> None:
    #     if(self.stack_num):
    #         self.stack_num.pop()
    #         self.stack_min.pop()
    #     else:
    #         pass
    # def top(self) -> int:
    #     if(self.stack_num):
    #         return self.stack_num[len(self.stack_num)-1]
    #     return None
    # def min(self) -> int:
    #     if(self.stack_min):
    #         return self.stack_min[len(self.stack_min)-1]
    def __init__(self):
        self.A, self.B = [], []

    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]

obj = MinStack()
obj.push(0)
obj.push(1)
# obj.push(-2)
obj.push(0)
print(obj.top())
print(obj.min())
obj.pop()
print(obj.top())
print(obj.min())
obj.pop()
print(obj.top())
print(obj.min())
obj.pop()
print(obj.top())
print(obj.min())
obj.pop()
print(obj.top())
print(obj.min())
obj.pop()
print(obj.top())
print(obj.min())