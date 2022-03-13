'''
大根堆中调用交换数据的函数
'''
import func_ChangeTwoParameters

def func(nums,start,end):
    for i in range(start+1,end):
        for j in range(start,i):
            n=i-j
            if(nums[n]>nums[int((n-1)/2)]):
                nums[n],nums[int((n-1)/2)]=func_ChangeTwoParameters.func(nums[n],nums[int((n-1)/2)])
