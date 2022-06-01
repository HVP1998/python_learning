'''
给定一个数组nums和滑动窗口的大小k,请找出所有滑动窗口里的最大值。
'''

from collections import deque
from typing import List
class Solution:
    # 无优化
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        list_max=[]
        if(not nums):return nums
        if(len(nums)==1):
            return nums
        for i in range(0,len(nums)-k+1):
            max=nums[i]
            for j in range(i+1,i+k):
                if(nums[j]>max):
                    max=nums[j]
            list_max.append(max)
        return list_max
    # 利用双向队列优化
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        if(not nums):return nums
        if(len(nums)==1):
            return nums
        list_max=list()
        deque_windows_max=deque()
        # 初始化窗递减队列
        deque_windows_max.append(nums[0])
        for i in range(1,k):
            while deque_windows_max and nums[i]>deque_windows_max[-1]:
                deque_windows_max.pop()
            deque_windows_max.append(nums[i])
        # 记录窗最大队列中的最大值
        list_max.append(deque_windows_max[0])
        # 对原队列进行遍历进行上述的两个步骤
        for i in range(k,len(nums)):
            if nums[i-k]==deque_windows_max[0]:
                deque_windows_max.popleft()
            while deque_windows_max and nums[i]>deque_windows_max[-1]:
                deque_windows_max.pop()
            deque_windows_max.append(nums[i])
            list_max.append(deque_windows_max[0])
        return list_max
    # 在双向队列优化的基础上合并循环
    def maxSlidingWindow3(self, nums: List[int], k: int) -> List[int]:
        # 当列表为空时
        if(not nums):return nums
        # 当列表只有一个数据时
        if(len(nums)==1):
            return nums
        # 数据初始化
        list_max=list()
        deque_windows_max=deque()
        deque_windows_max.append(nums[0])
        if(k==1):
            list_max.append(deque_windows_max[0])
        # 遍历列表
        for i in range(1,len(nums)):
            while deque_windows_max and nums[i]>deque_windows_max[-1]:
                deque_windows_max.pop()
            deque_windows_max.append(nums[i])
            if(i==k-1):
                list_max.append(deque_windows_max[0])
            if(i>k-1):
                if nums[i-k]==deque_windows_max[0]:
                    deque_windows_max.popleft()
                list_max.append(deque_windows_max[0])
        return list_max
    # 答案：利用双指针优化循环，增加循环的普遍性
    def maxSlidingWindow4(self, nums: List[int], k: int) -> List[int]:
        deque = deque()
        res, n = [], len(nums)
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            # 删除 deque 中对应的 nums[i-1]
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()
            # 保持 deque 递减
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            # 记录窗口最大值
            if i >= 0:
                res.append(deque[0])
        return res


nums = [1,3,-1,-3,5,3,6,7]
S=Solution()
# print(S.maxSlidingWindow1(nums,3))
print(S.maxSlidingWindow3(nums,5))
print(S.maxSlidingWindow3(nums,3))