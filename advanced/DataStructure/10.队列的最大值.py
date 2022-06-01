"""
定义一个队列并实现函数 max_value 得到队列里的最大值,要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。
"""


from collections import deque


class MaxQueue:
    # 利用列表代替队列
    # def __init__(self):
    #     self.stack_norm, self.stack_max = [], []

    # def max_value(self) -> int:
    #     return self.stack_max[0] if self.stack_norm else  -1

    # def push_back(self, value: int) -> None:
    #     self.stack_norm.append(value)
    #     while(self.stack_max) and self.stack_max[-1]<value:
    #         self.stack_max.pop()
    #     self.stack_max.append(value)

    # def pop_front(self) -> int:
    #     if not self.stack_norm:
    #         return -1
    #     if(self.stack_norm[0] == self.stack_max[0]):
    #         self.stack_max = self.stack_max[1:]
    #     max = self.stack_norm[0]
    #     self.stack_norm = self.stack_norm[1:]
    #     return max
    # 利用队列
    def __init__(self):
        self.stack_norm = deque()
        self.stack_max = deque()

    def max_value(self) -> int:
        return self.stack_max[0] if self.stack_norm else -1

    def push_back(self, value: int) -> None:
        self.stack_norm.append(value)
        while(self.stack_max) and (self.stack_max[-1]) < value:
            self.stack_max.pop()
        self.stack_max.append(value)

    def pop_front(self) -> int:
        if not self.stack_norm:
            return -1
        if(self.stack_norm[0] == self.stack_max[0]):
            self.stack_max.popleft()
        max = self.stack_norm[0]
        self.stack_norm.popleft()
        return max


# Your MaxQueue object will be instantiated and called as such:
obj = MaxQueue()
print(obj.max_value())
obj.push_back(-1)
print(obj.max_value())
obj.push_back(10)
print(obj.max_value())
obj.push_back(0)
print(obj.max_value())
obj.push_back(10)
print(obj.max_value())
obj.push_back(-1)
print(obj.max_value())
obj.push_back(0)
print(obj.max_value())
print("******************************************")
print(obj.pop_front())
print(obj.max_value())
print(obj.pop_front())
print(obj.max_value())
print(obj.pop_front())
print(obj.max_value())
print(obj.pop_front())
print(obj.max_value())
print(obj.pop_front())
print(obj.max_value())
print(obj.pop_front())
print(obj.max_value())
print(obj.pop_front())
print(obj.max_value())
