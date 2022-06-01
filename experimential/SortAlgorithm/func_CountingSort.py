# 计数排序


def func_loop(nums:int)->list:
    if(len(nums)<=1):return nums
    # 确定数组范围
    max,min=nums[0],nums[0]
    for i in range(1,len(nums)):
        if(max<nums[i]):max=nums[i]
        elif(min>nums[i]):min=nums[i]
    # 构造计数列表
    nums_count=[0]*(max-min+1)
    # 计数
    for i in range(0,len(nums)):
        nums_count[nums[i]-min]+=1
    for i in range(1,len(nums_count)):
        nums_count[i]=nums_count[i]+nums_count[i-1]
    # 排序,倒序遍历
    nums_sort=[0]*len(nums)
    for i in range(len(nums)-1,-1,-1):
        nums_count[nums[i]-min]-=1
        nums_sort[nums_count[nums[i]-min]]=nums[i]
    return nums_sort


if __name__=="__main__":
    nums1=[0,-1,10,9,5,8,9,6,1]
    nums2=[10]
    nums3=[]
    print(func_loop(nums1))
    print(func_loop(nums2))
    print(func_loop(nums3))