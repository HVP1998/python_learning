#*************
#1.将无序数组构造为大根堆
#2.将头节点与尾节点进行交换后构造大根堆
#3.多次进行step2后得到排序数组
#*************

"""
由于都是将数组排为大根堆
所以将排序为大根堆的过程写为函数
并在循环中调用
"""
import func_BigTree
import func_ChangeTwoParameters

nums=[3,6,8,5,7,2,10,1,9,4,4]
#由于直接对数组进行操作，所以不用返回值
for i in range(0,len(nums)-1):
    func_BigTree.func(nums,0,len(nums)-i)
    nums[0],nums[len(nums)-1-i]=func_ChangeTwoParameters.func(nums[0],nums[len(nums)-1-i])
    print(nums)
